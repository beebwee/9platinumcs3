class EditorialWriting:
    def __init__(self, headline, stand, argument, draft):
        self.headline = headline
        self.stand = stand
        self.argument = argument
        self.__draft = draft

    def research(self):
        print(f"Gathering research data for: '{self.headline}'...")
        self.__draft += "\n[Added research findings]"

    def criticize(self):
        print(f"Analyzing weaknesses in the stand '{self.stand}' and argument.")

    def establish_position(self, editorial: str):
        print(f"Aligning the writing with editorial direction...")
        self.stand = editorial


    if __name__ == "__main__":

    # Object 1: Education Editorial
    article1 = EditorialWriting(
        headline="Humanity Behind the Technology",
        stand="Pro-HUMSS",
        argument="HUMSS competitions should also be considered in the PSHS system aside from STEM.",
        draft="Draft V1: Focus on how students skilled in HUMSS are less recognized than STEM achievers."
    )

    # Object 2: Political Editorial
    article2 = EditorialWriting(
        headline="Fame Can Lead to Shame",
        stand="Anti-Corruption",
        argument="Not all famous leaders and people fulfill their promises to the public.",
        draft="Draft V1: Heavy focus on the heavy disadvantage of political dynasties."
    )

    # Display original states
    print(f"Object 1 Original Stand: {article1.stand}")
    print(f"Object 2 Original Stand: {article2.stand}")
    print("-" * 50)


     article1.establish_position("Strict Global Governance")
    article1.append_research("EU passes unified framework penalties.")

    print("\n--- Final Comparison Matrix ---")
    
    # Verify Object 1 reflecting the modifications
    print("[OBJECT 1 STATUS (Tech Editorial)]")
    print(f"  Headline: {article1.headline}")
    print(f"  Current Stand: {article1.stand} <-- (CHANGED)")
    print(f"  Private Draft Readout:\n  \"{article1.reveal_draft()}\" <-- (UPDATED)")
    
    print()

    # Verify Object 2 remains fully untouched and unchanged
    print("[OBJECT 2 STATUS (Political Editorial]")
    print(f"  Headline: {article2.headline}")
    print(f"  Current Stand: {article2.stand} <-- (UNCHANGED)")
    print(f"  Private Draft Readout:\n  \"{article2.reveal_draft()}\" <-- (UNCHANGED)")