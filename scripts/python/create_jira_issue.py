import os
import core

JIRA_SERVER = os.getenv("JIRA_SERVER", None)
JIRA_USERNAME = os.getenv("JIRA_USERNAME", None)
JIRA_TOKEN = os.getenv("JIRA_TOKEN", None)
JIRA_PROJECT = os.getenv("JIRA_PROJECT", None)
JIRA_TICKET_TYPE = os.getenv("JIRA_TICKET_TYPE", None)
JIRA_TICKET_SUMMARY = os.getenv("JIRA_TICKET_SUMMARY", None)
JIRA_TICKET_DESCRIPTION = os.getenv("JIRA_TICKET_DESCRIPTION", None)

WORKFLOW_RUN_LINK = os.getenv("WORKFLOW_RUN_LINK", None)


def main():
    core.set_output("link", JIRA_TICKET_SUMMARY)


if __name__ == "__main__":
    main()
