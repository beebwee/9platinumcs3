class ColumnWriting:
    def __init__(self, headline, columnist, commentary, anecdote):
        self.headline = headline
        self.columnist = columnist
        self.commentary = commentary
        self.anecdote = anecdote

    # Public visibility method
    def entertain(self, topic: str):
        print(f"[{self.columnist}] Entertaining about {topic} using: '{self.anecdote}'")
        self.__fact_check()  # Triggers private method

    # Private visibility method (uses double underscore)
    def __fact_check(self):
        print(f"   -> [VERIFYING] Fact-checking: '{self.headline}'... Done.")


class EditorialWriting:
    def __init__(self, headline, stand, argument, draft):
        self.headline = headline
        self.stand = stand
        self.argument = argument
        self.__draft = draft
        # 1:Many Relationship list to store actual objects
        self.related_columns = []

    # Method to build the relationship
    def add_column(self, column_object):
        self.related_columns.append(column_object)


if __name__ == "__main__":
    # --- STEP 8: Create the objects ---
    editorial = EditorialWriting("Tech & Humanity", "Pro-HUMSS", "Need balance", "Draft V1")

    col1 = ColumnWriting("Coffee Culture", "Juan dela Cruz", "Hustle is tiring", "Spilled my latte")
    col2 = ColumnWriting("AI Creativity", "Maria Santos", "AI needs humans", "Bot wrote a bad poem")
    col3 = ColumnWriting("Lost without Maps", "Roffe Fajardo", "GPS ruins instincts", "Got lost in a town")

    # --- STEP 11 A: Before Relationship ---
    print("--- BEFORE RELATIONSHIP ---")
    print(f"Editorial: {editorial.headline}")
    print(f"Columns attached to editorial: {len(editorial.related_columns)}")
    print()

    # --- STEP 11 B: Building Relationship ---
    print("--- BUILDING RELATIONSHIP ---")
    editorial.add_column(col1)
    editorial.add_column(col2)
    editorial.add_column(col3)
    print("Columns successfully referenced from the editorial object.")
    print()

    # --- STEP 11 C: After Relationship (Access via Loop) ---
    print("--- AFTER RELATIONSHIP ---")
    print(f"Editorial Anchor: {editorial.headline}")
    print("Related Column(s):")
    print("-" * 40)

    # Loop to access properties and methods through the relationship
    for col in editorial.related_columns:
        print(f"Column Headline: {col.headline}")
        print(f"Written By: {col.columnist}")
        col.entertain("Daily Life")
        print("-" * 40)
