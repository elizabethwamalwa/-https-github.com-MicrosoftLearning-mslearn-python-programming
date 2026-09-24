# This is my first attempt at independent coding
# I am learning Python
# This program will print out all the information about me


def introduction():
    print("Hello and welcome to my space!")

    name = "Wamalwa Elizabeth"
    job = "QA Engineer"
    goal = "Cloud Security Engineer"
    prg_lang = "Python"

    print(
        f"My name is {name} and I am a {job}. "
        f"I work exclusively on testing Windows products. "
        f"My ultimate goal is to be a {goal}. "
        f"I am a self-taught programmer and I am currently learning {prg_lang}."
    )

    print("I have amateur experience in cloud computing and some knowledge of cybersecurity.")
    print("Now that we are done with the introduction, let's move to the next part.")


def skills():
    print("\n\n")
    print("My skills include:")

    skills = [
        "Python programming",
        "Manual testing",
        "Bug reporting",
        "Cloud computing - Google Cloud Platform, AWS, Azure",
        "Cloud security fundamentals",
        "Cloud security architecture and design",
        "Cybersecurity - penetration testing",
        "Network security",
        "Reconnaissance",
        "Reporting",
        "Vulnerability assessment and management",
        "Linux",
        "Windows OS",
        "Networking fundamentals"
    ]

    for number, skill in enumerate(skills, start=1):
        print(f"{number}. {skill}")


def hobbies():
    print("\n\n")
    print("My hobbies include:")

    hobbies = [
        "Writing - I write a lot to process everything: pain, joy and sadness. My pen name is Ten, and I often introduce myself as Ten.",
        "Hiking - I love the mountains and outdoors. They have a tendency to make my problems feel small.",
        "Watching films - Films are my way of learning about cultures of the world.",
        "Cooking - This is how I show love.",
        "Reading - I read as obsessively as I write, about anything and everything.",
        "Travelling - The world really is beautiful, and I want to see as much of it as I can. Travelling exposes alternatives to my reality and enables me to see how humanity transcends language, colour and culture.",
        "Gardening - There is something beautiful about nurturing life from a seed to a plant and finally to something that can sustain life. It is a beautiful process and I love it.",
        "Swimming",
        "Cycling",
        "Running"
    ]

    for number, hobby in enumerate(hobbies, start=1):
        print(f"{number}. {hobby}")


def fun_facts():
    print("\n\n")

    print(
        "I don't believe in living a fixed life. "
        "I believe in exploring as much of yourself as you can "
        "and finding yourself in all dimensions."
    )

    print(
        "I chose to work in Tech because: "
        "1. It is a field that can help me bring change to the world in my own way. "
        "Through tech, people's lives can be improved, and being part of that makes me happy. "
        "2. Tech is a field that keeps me on my toes. It is always changing and evolving. "
        "Tech will not allow me to be comfortable, and I love that. "
        "3. I believe tech will give me the freedom to live and work in as many "
        "different countries as possible."
    )

    print("\n\n")

    print(
        "Countries I would like to live in and work in, in no particular order, include:"
    )

    countries = [
        "Germany",
        "Seoul, South Korea",
        "Austria",
        "Switzerland",
        "Canada",
        "New Zealand",
        "Australia",
        "Japan",
        "Singapore",
        "United Arab Emirates",
        "United States of America",
        "Italy",
        "Georgia",
        "China",
        "Seychelles",
        "Mauritius",
        "Nordic countries"
    ]

    for number, country in enumerate(countries, start=1):
        print(f"{number}. {country}")

    print("\n\n")

    experiences = [
        "Watching Christopher Tin in concert",
        "Christmas in Europe",
        "Christmas in New York",
        "Road tripping across the US",
        "Summers in Europe",
        "Nightlife in Asia",
        "Kingfisher concert",
        "Ela Mai concert",
        "Road tripping across Africa",
        "Life in Central Asia",
        "A very diverse life with a very diverse group of friends"
    ]

    print("Some of the things I want to experience in life include:")

    for number, experience in enumerate(experiences, start=1):
        print(f"{number}. {experience}")

    print("\n\n")

    print(
        "Outside of caring for Tech and how it can be used to improve people's lives, "
        "I care about the environment, and in particular sustainable practices, "
        "ocean conservation and preservation of marine life, renewable energy, "
        "providing affordable housing solutions through alternative inexpensive "
        "building solutions, agro-manufacturing and reducing post-harvest losses "
        "by up to 70% in Kenya, waste management through recycling and upcycling, "
        "and increasing Kenya's forest cover."
        "i believe in the power of an empowerd society"
        
    )

    print(
        "I look forward to the day Kenya's streets will be clean and free of waste, "
        "where our parks will be a comprehensive third space and Nairobi will be "
        "known as the green city."
    )
    print(
        "My favourite quote is:"
        "There is no exquisite beauty without some strangeness in the proportion.”
        — Edgar Allan Poe"
    )


# Calling the functions

introduction()
skills()
hobbies()
fun_facts()