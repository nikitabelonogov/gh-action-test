import os
import core
from jira import JIRA


def main():
    JIRA_SERVER = os.getenv("JIRA_SERVER", None)
    JIRA_USERNAME = os.getenv("JIRA_USERNAME", None)
    JIRA_TOKEN = os.getenv("JIRA_TOKEN", None)
    JIRA_PROJECT = os.getenv("JIRA_PROJECT", None)
    JIRA_TICKET_TYPE = os.getenv("JIRA_TICKET_TYPE", None)
    JIRA_TICKET_SUMMARY = os.getenv("JIRA_TICKET_SUMMARY", None)
    JIRA_TICKET_DESCRIPTION = os.getenv("JIRA_TICKET_DESCRIPTION", None)
    WORKFLOW_RUN_LINK = os.getenv("WORKFLOW_RUN_LINK", None)

    jira_client = JIRA(JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_TOKEN))
    issue_dict = {
        'project': {'key': JIRA_PROJECT},
        'summary': JIRA_TICKET_SUMMARY,
        'description': JIRA_TICKET_DESCRIPTION,
        'issuetype': {'name': JIRA_TICKET_TYPE},
    }
    new_issue = jira_client.create_issue(fields=issue_dict)
    new_issue_link = f"{JIRA_SERVER}/browse/{new_issue.key}"
    print(f"A new Jira issue is created {new_issue.key} {new_issue_link}")
    core.set_output("key", new_issue.key)
    core.set_output("link", new_issue_link)

    if WORKFLOW_RUN_LINK:
        comment = '''> '''
        jira_client.add_comment(new_issue, comment)


if __name__ == "__main__":
    main()
