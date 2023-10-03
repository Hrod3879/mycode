challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

def challenge_output():
    a= challenge[2][1]
    b= challenge[2][0]
    c= challenge[3]

    print(f"My {a}! The {b} do {c}!")


def trial_output():
    a= trial[2]["goggles"]
    b= trial[2]["eyes"]
    c= trial[-1]

    print(f"My {a}! The {b} do {c}!")


def nightmare_output():
    a= nightmare[0]["user"]["name"]["first"]
    b= nightmare[0]["kumquat"]
    c= nightmare[0]["d"]
    
    print(f"My {a}! The {b} do {c}!")
    
nightmare_output()
trial_output()
challenge_output()

