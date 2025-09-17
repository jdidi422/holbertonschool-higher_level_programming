import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files based on a template.

    :param template: A string containing placeholders for the invitation.
    :param attendees: A list of dictionaries with details about attendees.
    """

    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if (not isinstance(attendees, list) or
            not all(isinstance(att, dict) for att in attendees)):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee and create an invitation
    for index, attendee in enumerate(attendees, start=1):
        # Replace missing values with "N/A"
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Replace placeholders in the template
        invitation_content = (
            template.replace("{name}", name)
                    .replace("{event_title}", event_title)
                    .replace("{event_date}", str(event_date))
                    .replace("{event_location}", event_location)
        )

        # Generate output filename
        output_filename = f"output_{index}.txt"

        # Write the invitation to the file
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(invitation_content)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")