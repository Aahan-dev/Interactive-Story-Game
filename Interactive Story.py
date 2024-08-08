class InteractiveStory:
    def __init__(self):
        """Initialize the interactive story with a starting point."""
        self.story = {
            'start': {
                'text': "You find yourself in a dark forest. You can go left or right.",
                'choices': {
                    'left': 'left_path',
                    'right': 'right_path'
                }
            },
            'left_path': {
                'text': "You encounter a friendly deer. Do you want to pet it or continue walking?",
                'choices': {
                    'pet': 'deer_pet',
                    'continue': 'continue_walk'
                }
            },
            'right_path': {
                'text': "You stumble upon a hidden treasure! Do you want to take it or leave it?",
                'choices': {
                    'take': 'take_treasure',
                    'leave': 'leave_treasure'
                }
            },
            'deer_pet': {
                'text': "The deer leads you to a beautiful clearing. You found peace!",
                'choices': {}
            },
            'continue_walk': {
                'text': "You walk deeper into the forest and get lost. Game over.",
                'choices': {}
            },
            'take_treasure': {
                'text': "You take the treasure and become rich! The end.",
                'choices': {}
            },
            'leave_treasure': {
                'text': "You leave the treasure and continue your adventure. The end.",
                'choices': {}
            }
        }

    def get_story(self, section):
        """Return the story text and choices for the given section."""
        return self.story[section]['text'], self.story[section]['choices']


    def run(self):
        """Run the interactive story until the user reaches an ending."""
        current_section = 'start'
       
        while True:
            text, choices = self.get_story(current_section)
            print(text)
           
            # If there are no choices, the story ends
            if not choices:
                break
           
            # Display choices
            print("What do you want to do?")
            for choice in choices:
                print(f"- {choice}")


            # Get user input for the next choice
            user_choice = input("Choose an option: ").strip().lower()
           
            # Validate user choice
            if user_choice in choices:
                current_section = choices[user_choice]
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Create an instance of InteractiveStory and run it
    story = InteractiveStory()
    story.run()
