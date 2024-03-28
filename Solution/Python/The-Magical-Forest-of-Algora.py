from openai import OpenAI

client = OpenAI(api_key="", base_url="")

print(client.models.list())

class MagicalCreature:
    def __init__(self, name, move):
        self.name = name
        self.move = move

    def dance(self):
        return self.move


class AlgoraForest:
    def __init__(self, creature1, creature2):
        self.creature1 = creature1
        self.creature2 = creature2
        self.effects = {
            ("Twirl", "Twirl"): "Fireflies light up the forest.",
            ("Leap", "Spin"): "Gentle rain starts falling.",
            ("Spin", "Leap"): "A rainbow appears in the sky.",
        }

    def start_dance(self):
        move1 = self.creature1.dance()
        move2 = self.creature2.dance()
        print(f"{self.creature1.name} did {move1} and {self.creature2.name} did {move2}")
        effect = self.effects.get((move1, move2), "A magical effect you can't comprehend!")
        print(effect)


name1 = input("Enter the name of the first creature: ")
move1 = input("Enter the dance move of the first creature: ")
creature1 = MagicalCreature(name1, move1)

name2 = input("Enter the name of the second creature: ")
move2 = input("Enter the dance move of the second creature: ")
creature2 = MagicalCreature(name2, move2)

forest = AlgoraForest(creature1, creature2)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url