from data_types.offer import Offer
from data_types.research import Research


def save_scraped_data(research: Research) -> None:
    """
    Save the scraped data to a file.
    Args:
        research (Research): The research object.
    Returns:
        None
    """
    print("Saving scraped data...")
    with open("scraped_jobs.txt", "w", encoding="utf-8") as f:
        f.write(f"Total Job: {len(research.offers)}\n\n")

        f.write(f"Locations ({len(research.locations)})\n")
        for location in research.locations:
            f.write(f"- {location}\n")
        f.write("\n")

        f.write(f"Companies ({len(research.companies)})\n")
        for company in research.companies:
            f.write(f"- {company}\n")
        f.write("\n")

        for offer in research.offers:
            # Write each offer's details on a new line
            f.write("-" * 50 + "\n")  # Separator between offers
            f.write(f"{offer.title.upper()}\n")
            f.write(f"Company: {offer.company}\n")
            f.write(f"Location: {offer.location}\n")
            f.write(f"Mode: {offer.mode}\n")
            f.write(f"Salry: {offer.salary}\n")
            f.write(f"Publisehd: {offer.published}\n")
            f.write("-" * 50 + "\n")  # Separator between offers

    print("Data saved")
