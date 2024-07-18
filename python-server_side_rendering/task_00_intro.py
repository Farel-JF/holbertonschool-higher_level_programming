#!/usr/bin/env python3
"""
Script to generate personalized invitation files
based on a template and list of attendees.
"""

import os

# Define the invitation template
template = """
Dear {name},

You are invited to attend {event_title} on {event_date} at {event_location}.

We hope to see you there!

Best regards,
Organizing Committee
"""

# Define the list of attendees with their details
attendees = [
    {"name": "Alice", "event_title": "Annual Gala Dinner",
    "event_date": "July 25, 2024", "event_location": "Grand Ballroom"},
    {"name": "Bob", "event_title": "Tech Conference", "event_date":
    "August 10, 2024", "event_location": "Convention Center"},
]

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees should be a list.")
        return
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Each attendee should be a dictionary.")
            return

    # Check for empty input
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Write to output file
        output_filename = f"output_{index}.txt"
        with open(output_filename, "w") as f:
            f.write(invitation)

        # Print confirmation message
        print(f"Invitation for {attendee['name']} generated: {output_filename}")

