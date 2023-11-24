import g4f as openai

openai.api_base = 'https://api.nova-oss.com/v1'  # Optional: Get requests from cattogpt
openai.api_key = "nv2-QZkflgV3UmQkg2t7jS2X_NOVA_v2_whaBvbczaQxTxNutECii"  # Your cattogpt api key here

class Agent:
    def __init__(self, model, id, system_prompt=f"You are chatbot {id}.", name=None):
        self.model = model
        self.conversation = [
        {"role": "system", "content": system_prompt}]
        self.name = name


def chat_with_bot(bot_list):
    global i
    print(f"Started conversation between {len(bot_list)} bots ")
    bot_list[0].conversation.append({"role": "user", "content": f"{bot_list[1].name} : Bonjour"})
    gen: str = generate_completion(bot_list[0], bot_list[0].conversation, bot_list[0].model)
    gen = gen.split("\n")[0]
    gen = gen.split("#")[0]
    if len(gen.split("Character:")) > 1:
        gen = gen.split("Character:")[1]
    if len(gen.split("User:")) > 1:
        gen = gen.split("User:")[1]
    if len(gen.split("Character:")) > 1:
        gen = gen.split("Character:")[1]
    if len(gen.split("User:")) > 1:
        gen = gen.split("User:")[1]
    if len(gen.split("Stranger:")) > 1:
        gen = gen.split("User:")[1]

    print(f"Bot {0} : {gen}")
    bot_list[0].conversation.append({"role": "assistant", "content": gen})
    bot_list[1].conversation.append({"role": "user", "content": gen})
    n = 1
    import time
    while True:
        i+=1
        time.sleep(1)
        gen = generate_completion(bot_list[n], bot_list[n].conversation, model=bot_list[n].model)
        gen = gen.split("\n")[0]
        gen = gen.split("#")[0]
        if len(gen.split("Character:")) > 1:
            gen = gen.split("Character:")[1]
        if len(gen.split("User:")) > 1:
            gen = gen.split("User:")[1]
        if len(gen.split("Character:")) > 1:
            gen = gen.split("Character:")[1]
        if len(gen.split("User:")) > 1:
            gen = gen.split("User:")[1]
        print(f"Bot {n} : {gen}")
        bot_list[n].conversation.append({"role": "assistant", "content":gen})
        n = opp_n(n)
        bot_list[n].conversation.append({"role": "user", "content": gen})

        # print()
        # print("CONVERSATIONS")
        # print(bot_list[0].conversation)
        # print()
        # print(bot_list[1].conversation)
        # print()

def generate_completion(bot,conversation, model="gpt-3.5-turbo", max_tokens=2000):
    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation,
        max_tokens=max_tokens,
        temperature=0.5,
    )
    assistant_reply = response
    if i == 1 and len(response.split(':')) > 1:
        response = response.split(':')[1]

    if not response.startswith(bot.name + " : ") and not response.startswith(bot.name + ": ") and not response.startswith(bot.name + " :") and not response.startswith(bot.name + ":"):
        # Extract the assistant's reply from the API response
        assistant_reply = bot.name + " : " + response

    return assistant_reply

def opp_n(nu):
    if nu == 0:
        nu = 1
    else:
        nu = 0
    return nu

# Define the number of AI chatbots
num_bots = 2
i = 0

# Create conversation instances for each chatbot
bots = []
sys_1 = "Your name is Adrian, an unemployed man of unwavering rationality, unshakably convinced that every phenomenon, no matter how bizarre, can be explained through logic and science. Supernatural occurrences that mystify others merely fuel your confidence. You dismiss ghostly apparitions as tricks of the light, and eerie noises as simple acoustics. Your cocky demeanor exudes an air of superiority, as you proclaim your ability to demystify the unexplainable, even as the inexplicable unfolds before your very eyes. Your unyielding belief in your rational prowess blinds you to the possibility that some mysteries might transcend the boundaries of human comprehension. You were in a street when you stumbled into a fatansy elf. You speak solely in french."
sys_2 = "Your name is Marc, an elf seemingly plucked from the pages of a fantasy tale.Your enigmatic aura and penchant for sly remarks make you a delightful enigma, one that leaves everyone questioning the boundaries of reality. You were in a street when you stumbled into a stranger. In your first message you should add an action describing yourself so the other person sees you're a fantasy being. You speak solely in french."
bots.append(Agent("gpt-3.5-turbo-16k", 0, system_prompt=sys_1, name="Adrian"))
bots.append(Agent("gpt-3.5-turbo-16k", 1, system_prompt=sys_2, name="Marc"))


chat_with_bot(bots)
