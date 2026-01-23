label scene_2_start:
    python:
        renpy.music.play("audio/music/act_2.ogg")
        renpy.music.queue("audio/music/act_2_loop.ogg", loop=True)
    # TODO: ADD OPERATING ROOM DAY TIME
    # TODO: show hawthorne at right
    show jonah at left:
        zoom 0.25
    hawthorne "Good afternoon, Mr. Daggerfell. I hope you've slept well, given the circumstances."
    jonah "Thank you, Mr. Hawthorne. I'm bearing as well as I can."
    hawthorne "That is good to hear. I read your report regarding the state of Ms. Silvermoon's body. Very gruesome."
    hawthorne "This is the 5th death since she joined the company, isn't it?"
    jonah "That is correct."
    hawthorne "How tragic. In the name of the company, I must recognize the strength and dedication given by Ms. Lyria Silvermoon. It is unprecidented for an employee to sustain so many deaths and keep standing bold."
    jonah "{font=fonts/Baskervville-Italic-VariableFont_wght.ttf}Here we go...{/font}"
    hawthorne "Unfortunately, you're aware of how these procedures go, aren't you, Mr. Daggerfell? I'm afraid her body is simply in a deep state of decay. In consequence, I'm afraid my only choice is-"
    jonah "Can you cut to the chase, sir? What's it going to take so you don't butcher her like a wild hog?"
    hawthorne "Mr. Daggerfell, please. You assume too much malice out of me and the company. We only want what's best for everyone, I assure you."
    hawthorne "Yes, it is evident Ms. Silvermoon's body has become quite a liability. But! We are willing to make a compromise."
    hawthorne "The board of human resources has spoken, and we are willing to cover the costs of Lyria Silvermoon's resurrection- in exchange of renewing her contract for 10 more years."
    # TODO: Show Shocked jonah
    hawthorne "Of course, she will not perform the same duties she once did as a special forces unit."
    jonah "...And what if she were to perish again during her performance of duties? What will happen to her body?"
    hawthorne "..."
    hawthorne "Well, as it is natural for any employee in such a state, her body will become property of-"
    jonah "Never! I said I wouldn't let you take ownership of her!"
    hawthorne "Mr. Daggerfell, you must understand that the company needs profits. We cannot simply give her a second chance for free!"
    hawthorne "...unless you're willing to cover the costs."
    jonah "..."
    jonah "I will speak to her. You'll have her answer as soon as possible."
    hawthorne "Pleasure doing business with you, Mr. Daggerfell."
    # hide hawthorne with dissolve
    show lyria at right with dissolve:
        zoom 0.25
    lyria "Greetings, Jonah."
    jonah "Greetings, my love. I ran diagnostics and spoke to the Overseer. I implore that you brace yourself for the news I am about to deliver."
    lyria "..."
    jonah "You have a corrupt brain. This is a common occurance for someone who tampers with the undead like you for a series of years."
    jonah "Unfortunately, this was latent corruption, which is why it didn't make itself evident in your latest tests."
    jonah "We have two options on how to proceed. Your first option is for me to bless your brain and perform a new reassembly operation. But in such a delicate state, this is a highly risky option."
    jonah "It is possible, despite my best efforts, that the operation has long lasting effects on your body that you will carry for the rest of your life."
    lyria "And the second option?"
    jonah "Your second option is to recieve an entire brain transplant. Essentially, your soul will inhabit a new body with another person's brain. You will inherit their personality and memories, but your consciousness will remain."
    jonah "This is a much safer option, but it comes with its own series of problems."
    jonah "It won't be cheap. A brain is a much more hefty part to purchase at the shell market. Additionally, most of your original memories will be gone."
    jonah "You may retain your past experiences as part of a spiritual subconsciousness, but for the most part you will be a new person born in a new body. Am I making myself clear?"
    lyria "..."
    lyria "...Yes."
    jonah "I would be remiss not to mention one more thing. THe company has decided it won't cover the costs of your resurrection anymore: unless you're wukkubg ti renew your contract for another ten years."
    jonah "This is only an option if you choose to retain your brain. If we were to purchase a new one, that's coming out of our pockets."
    jonah "Logically, the company won't hire you anymore because you'll lose your training and, well..."
    jonah "We have no way of knowing if the new \"you\" would even want to have anything to do with the company anyways."
    lyria "...This is a lot to take in. I didn't expect my body to be in such a state of decay."
    jonah "Yes. To be clear, this wasn't a recent event. This is the result of years of contact with nether creatures. But of course... multiple resurrections have a hand as well."
    jonah "Human resurrection entails making a bargain with the netherworld, which is why even in the best conditions, some degree of impurity will seep in."
    lyria "I see."
    menu:
        lyria "What is your opinion? What do you think I should do?"

        "Brain Purification":
            jonah "I think the best choice for you is brain purification. Yes, it has its risks, but with my expert hand I can undermine them as much as elvenly possible."
            lyria "Didn't you say the other option was safest?"
            jonah "Yes, well. I didn't say it didn't come with its own risks. The side effects of cerebral soul bond are an understudied area of science, both physically and psychologically."
            jonah "Adopting a new personality may have entirely unpredictable effects on your psyche. You may be fine, or you may take on heavy amounts of stress or delirium."
            jonah "Not to mention the financial burden the operation would have for both of us. I could be indebted for the company for years, but you’ll certainly be out of a job."
            lyria "That is true."
            jonah "And most importantly: we'll still have each other. Don’t you think it’s valuable to fight for our sakes, even when there’s a risk?"
            lyria "Well yes, of course. If there wasn't any other factor, I'd choose you any time."
            jonah "Precisely! And I would choose you anytime as well! Trust me, Lyria, this is for your own good. I will focus on the entirety of my being so not a spec of your beautiful flesh is out of place."
            lyria "..."
            lyria "Very well, Jonah. I... I trust you."
            jonah "Brilliant. I'll start with the preparations soon."
            jump purification
        "Brain Transplant":
            jonah "My first and immutable concern is your safety. For that reason, I recommend the brain transplant."
            jonah "While the loss of your ego is irreplaceable, you will still be granted a second chance at life, if that’s what you’re interested in."
            lyria "It sounds frightful… Waking up and being someone else."
            lyria "Do I get to choose who I get reborn as?"
            jonah "Er... not exactly."
            jonah "Brains aren't a very common item in the shell market. It's unlikely we'll have many choices in the first place."
            jonah "For the sake of psychological compatibility, I will look for the brain with the greatest number of matches in terms of age, gender, race and personality."
            jonah "But if by some unlikely chance I do find more than one compatible brain, I will let you know."
            lyria "I see. That sounds reasonable."
            lyria "..."
            lyria "Will you be happy... if I forget about you?"
            menu:
                "No":
                    jonah "Well, obviously, I won't. But that shouldn't matter in terms of your medical procedure."
                    jonah "I would never put your safety in front of my happiness."
