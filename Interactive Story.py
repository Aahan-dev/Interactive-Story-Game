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

    