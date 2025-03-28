import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.
    
    Args:
        template (str): A string containing the invitation template with placeholders.
        attendees (list): A list of dictionaries containing attendee data.
    """
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Handle empty template
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    
    # Handle empty list of attendees
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        invitation_text = template
        
        # Replace placeholders with actual values, or "N/A" if missing
        for key in ["name", "event_title", "event_date", "event_location"]:
            invitation_text = invitation_text.replace(f"{{{key}}}", attendee.get(key, "N/A") or "N/A")
        
        # Generate output file name
        output_filename = f"output_{index}.txt"
        
        # Write invitation to file
        try:
            with open(output_filename, "w") as file:
                file.write(invitation_text)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")