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

    # Private visibility method
    def __fact_check(self):
        print(f"   -> [VERIFYING] Fact-checking: '{self.headline}'... Done.")


class EditorialWriting:
    def __init__(self, headline, stand, argument, draft):
        self.headline = headline
        self.stand = stand
        self.argument = argument
        self.__draft = draft
        
        self.related_columns = []

   
    def add_column(self, column_object):
        self.related_columns.append(column_object)


if __name__ == "__main__":
    editorial = EditorialWriting("Tech & Humanity", "Pro-HUMSS", "Need balance", "Draft V1")

    col1 = ColumnWriting("Coffee Culture", "Juan dela Cruz", "Hustle is tiring", "Spilled my latte")
    col2 = ColumnWriting("AI Creativity", "Maria Santos", "AI needs humans", "Bot wrote a bad poem")
    col3 = ColumnWriting("Lost without Maps", "Roffe Fajardo", "GPS ruins instincts", "Got lost in a town")

    print("--- BEFORE RELATIONSHIP ---")
    print(f"Editorial: {editorial.headline}")
    print(f"Columns attached to editorial: {len(editorial.related_columns)}")
    print()

    print("--- BUILDING RELATIONSHIP ---")
    editorial.add_column(col1)
    editorial.add_column(col2)
    editorial.add_column(col3)
    print("Columns successfully referenced from the editorial object.")
    print()

    print("--- AFTER RELATIONSHIP ---")
    print(f"Editorial Anchor: {editorial.headline}")
    print("Related Column(s):")
    print("-" * 40)

    for col in editorial.related_columns:
        print(f"Column Headline: {col.headline}")
        print(f"Written By: {col.columnist}")
        col.entertain("Daily Life")
        print("-" * 40)
