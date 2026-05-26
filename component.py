from dataclasses import dataclass
from typing import Optional, Dict, Any
import requests
import json
import time
import re


@dataclass
class LastStep:
    thought: str
    action: str
    action_input: str
    action_result: str
    result: Optional[str] = None


class CrewApiForm:
    def __init__(self, base_url: str, bearer_token: str):
        """
        Initialize the CrewApiForm.
        
        Args:
            base_url: The base URL for the Crew API
            bearer_token: The Bearer token for authentication
        """
        self.base_url = base_url
        self.bearer_token = bearer_token
        
        # Form state
        self.repository_owner = ""
        self.issue_number = ""
        self.repository_name = ""
        self.documentation_experts = ""
        self.devops_experts = ""
        self.team_members_with_expertise = ""
        self.backend_experts = ""
        self.frontend_experts = ""
        
        # Status tracking
        self.task_id = ""
        self.state = ""
        self.status = ""
        self.last_step: Optional[LastStep] = None
        self.result: Optional[str] = None
        self.is_loading = False

    def submit(self) -> None:
        """Submit the form and start the crew."""
        self.is_loading = True
        try:
            kickoff_response = requests.post(
                f"{self.base_url}/kickoff",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.bearer_token}"
                },
                json={
                    "inputs": {
                        "repository_owner": self.repository_owner,
                        "issue_number": self.issue_number,
                        "repository_name": self.repository_name,
                        "documentation_experts": self.documentation_experts,
                        "devops_experts": self.devops_experts,
                        "team_members_with_expertise": self.team_members_with_expertise,
                        "backend_experts": self.backend_experts,
                        "frontend_experts": self.frontend_experts
                    }
                }
            )
            kickoff_data = kickoff_response.json()
            self.task_id = kickoff_data.get("kickoff_id")
            self.poll_status(self.task_id)
        except Exception as error:
            print(f"Error starting crew: {error}")
            self.is_loading = False

    @staticmethod
    def parse_last_step(last_step: Dict[str, str]) -> LastStep:
        """
        Parse the last step data from the API response.
        
        Args:
            last_step: Dictionary containing action and result
            
        Returns:
            LastStep object with parsed data
        """
        action = last_step.get("action", "")
        
        thought_match = re.search(r"Thought:\s*(.*?)\s*(?=(Action:|$))", action, re.DOTALL)
        action_match = re.search(r"Action:\s*(.*?)\s*(?=(Action Input:|$))", action, re.DOTALL)
        action_input_match = re.search(r"Action Input:\s*(.*)", action, re.DOTALL)
        result_input_match = re.search(r"Result:\s*(.*)", action, re.DOTALL)
        
        thought = thought_match.group(1).strip() if thought_match else ""
        action_str = action_match.group(1).strip() if action_match else ""
        action_input = action_input_match.group(1).strip() if action_input_match else ""
        action_result = result_input_match.group(1).strip() if result_input_match else ""
        
        return LastStep(
            thought=thought,
            action=action_str,
            action_input=action_input,
            action_result=action_result,
            result=last_step.get("result")
        )

    def poll_status(self, task_id: str) -> None:
        """
        Poll the status of the task.
        
        Args:
            task_id: The ID of the task to poll
        """
        try:
            status_response = requests.get(
                f"{self.base_url}/status/{task_id}",
                headers={
                    "Authorization": f"Bearer {self.bearer_token}"
                }
            )
            status_data = status_response.json()
            
            self.state = status_data.get("state", "")
            self.status = status_data.get("status", "")
            self.last_step = self.parse_last_step(status_data.get("last_step", {})) if status_data.get("last_step") else None
            self.result = status_data.get("result")
            
            if self.state == "SUCCESS":
                self.is_loading = False
            else:
                # Poll again after 10 seconds
                time.sleep(10)
                self.poll_status(task_id)
        except Exception as error:
            print(f"Error fetching status: {error}")
            # Retry after 10 seconds
            time.sleep(10)
            self.poll_status(task_id)

    def display_status(self) -> None:
        """Display the current status."""
        if self.task_id and self.state != "SUCCESS":
            print(f"Task ID: {self.task_id}")
            print(f"State: {self.state}")
            print(f"Status: {self.status}")

    def display_last_step(self) -> None:
        """Display the last step details."""
        if self.status and self.status != "SUCCESS" and self.last_step:
            print("\n=== Last Step Details ===")
            if self.last_step.thought:
                print(f"Thought:\n{self.last_step.thought}\n")
            if self.last_step.action:
                print(f"Action:\n{self.last_step.action}\n")
            if self.last_step.action_input:
                print(f"Action Input:\n{self.last_step.action_input}\n")
            if self.last_step.result:
                print(f"Action Result:\n{self.last_step.result}\n")

    def display_result(self) -> None:
        """Display the final result."""
        if self.result:
            print("\n=== Final Result ===")
            print(self.result)


# Example usage
if __name__ == "__main__":
    form = CrewApiForm(
        base_url="https://api.example.com",
        bearer_token="your-bearer-token"
    )
    
    # Set form fields
    form.repository_owner = "owner"
    form.issue_number = "123"
    form.repository_name = "repo-name"
    form.documentation_experts = "expert1, expert2"
    form.devops_experts = "devops1, devops2"
    form.team_members_with_expertise = "member1, member2"
    form.backend_experts = "backend1, backend2"
    form.frontend_experts = "frontend1, frontend2"
    
    # Submit and process
    form.submit()
    form.display_status()
    form.display_last_step()
    form.display_result()
