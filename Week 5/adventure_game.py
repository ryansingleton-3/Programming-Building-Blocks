first_level = input("You are flying in a private jet and you see one of the engines catch on fire. Your stomach drops as you feel the aircraft start to descend rapidly. Do you stay where you are and SCREAM, or GRAB an oxygen mask? ")
if first_level.lower() == "scream":
    print()
    print("Why are you screaming? Thats not going to help you.")
    second_level_scream = input("Because you chose to sit there and scream, you passed out during the plane crash because you couldn't breath. You wake up, still strapped in to your seat, but the seat was detached from the plane. It is night time, and you are dazed and confused. Your seatbelt won't budge, and seems to be stuck. Do you SCREAM again, or LOOK for something to cut it loose? ")
    if second_level_scream.lower() == "scream":
        print()
        print("Wow, you just keep making good decision after good decision.")
        third_level_scream_scream_ = input("After you scream at the top of your lungs, you attract the attention of a grizzly bear. He starts to approach you, and you feel your heart racing. Will you choose to SCREAM one last time, PRETEND you are dead, or GRAB a sharp piece of metal that you failed to see before because you were screaming, and use it to cut your seatbelt and free yourself? ")
        if third_level_scream_scream_.lower() == "scream":
            print("The grizzly bear got tired of hearing you scream, and mauled you to death. Game over.")
        elif third_level_scream_scream_.lower() == "pretend":
            print("The bear believes you are dead, and walks away after a few minutes. Some other passengers find you and you are able to get to safety.")
        elif third_level_scream_scream_.lower() == "grab":
            print("You grabbed the piece of metal and were able to cut yourself free. However, you cut your own hand very deeply with the metal when you used it. You are able to hide behind another part of the plane and the bear leaves. You get to safety, but your hand ends up getting amputated.")
        else:
            input("Not a valid option. Please choose SCREAM, PRETEND, or GRAB")
            if third_level_scream_scream_.lower() == "scream":
                print("The grizzly bear got tired of hearing you scream, and mauled you to death. Game over.")
            elif third_level_scream_scream_.lower() == "pretend":
                print("The bear believes you are dead, and walks away after a few minutes. Some other passengers find you and you are able to get to safety.")
            elif third_level_scream_scream_.lower() == "grab":
                print("You grabbed the piece of metal and were able to cut yourself free. However, you cut your own hand very deeply with the metal when you used it. You are able to hide behind another part of the plane and the bear leaves. You get to safety, but your hand ends up getting amputated.")
    elif second_level_scream.lower() == "look":
        print()
        third_level_scream_look = input("You look around, and find a sharp piece of metal from the wreckage. You carefully grab the metal and cut yourself free. You walk away from the wreckage and hear the rushing sound of water. As you approach the sound, you realize you are standing on the edge of a deep canyon, with a rushing river far below. You are very thirsty and tired. There is no visible way to get to the water without going deeper into the forest by following the river. You could JUMP off the cliff and into the river, FOLLOW the river downstream in hopes of finding a safer way to quench your thirst, or CLIMB up a tree and stay there for the night and get better visibility in the morning. ")
        if third_level_scream_look.lower() == "jump":
            print("You survived a plan crash, and choose to jump off a cliff? When you jump, you plunge over 300 feet to your death. You land on a a pile of rocks built up in the river and die on impact.")
        elif third_level_scream_look.lower() == "follow":
            print("You follow the river downstream and are able to find a spot about 1 mile away from the canyon where you are able to drink some water. You sprain your ankle, but you survive and are able to be rescued the next day.")
        elif third_level_scream_look.lower() == "climb":
            print("You climb a tree and wait there the rest of the night. Turns out, the tree you climbed was a maple tree, and you were able to drink some of the sap. You get rescued the next day and are able to stay out of harm's way.")
        else:
            input("Not a valid option. Please choose JUMP, FOLLOW, or CLIMB. ")
            if third_level_scream_look.lower() == "jump":
                print("You survived a plan crash, and choose to jump off a cliff? When you jump, you plunge over 300 feet to your death. You land on a a pile of rocks built up in the river and die on impact.")
            elif third_level_scream_look.lower() == "follow":
                print("You follow the river downstream and are able to find a spot about 1 mile away from the canyon where you are able to drink some water. You sprain your ankle, but you survive and are able to be rescued the next day.")
            elif third_level_scream_look.lower() == "climb":
                print("You climb a tree and wait there the rest of the night. Turns out, the tree you climbed was a maple tree, and you were able to drink some of the sap. You get rescued the next day and are able to stay out of harm's way.")




if first_level.lower() == "grab":
    print()
    print("Nice choice.")
    second_level_grab = input("You grab the oxygen mask, and are able to calm down as you take deep breathes. You hear the captain tell you to grab a parachute from underneath the seat. He says it is going to be a crash landing, and if we get out soon enough, we can land safely near a body of water. He also says that he is going to try to take it down in a flat part of land near the woods. You can choose to either JUMP out of the plane with a parachute on or STAY with the plane and the pilot and trust he can land the plane safely. ")
    if second_level_grab.lower() == "jump":
        print()
        print("What a daredevil.")
        third_level_grab_jump = input("You jump out of the airplane with your parachute on. However, as you fall rapidly and see the earth getting closer and closer, you start to panic. Your parachute is stuck and you immediately start to regret your decision to jump. However, you are able to give one last hard tug on your ripcord, and the parachute opens. You are more or less able to steer, and you have two spots you think look promising to land on. It is a heavily wooded area. You can either aim for a RIVERBANK or the foot of a MOUNTAIN. ")
        if third_level_grab_jump.lower() == "riverbank":
            print("You end up landing on the riverbank, but a heavy wind gust pulls you into the river before you can get your parachute off. You are able to free yourself, and then get a much needed drink from the river. You are soaking wet and dont get any sleep that night, but you get rescued the next day and get to safety.")
        elif third_level_grab_jump.lower() == "mountain":
            print("You aim for the perfect spot at the foot of the mountain but a huge wind gust pushes you off course and you slam into the mountainside. This knocks you out for a few days, during which a mountain lion finds you and eats you. Game over. ")
        else:
            input("Not a valid option. Please choose RIVERBANK, or MOUNTAIN")
            if third_level_grab_jump.lower() == "riverbank":
                print("You end up landing on the riverbank, but a heavy wind gust pulls you into the river before you can get your parachute off. You are able to free yourself, and then get a much needed drink from the river. You are soaking wet and dont get any sleep that night, but you get rescued the next day and get to safety.")
            elif third_level_scream_scream_.lower() == "mountain":
                print("You aim for the perfect spot at the foot of the mountain but a huge wind gust pushes you off course and you slam into the mountainside. This knocks you out for a few days, during which a mountain lion finds you and eats you. Game over.")      
    elif second_level_grab.lower() == "stay":
        print()
        third_level_scream_look = input("You are the only person that chooses to stay, and the captain tells you to come up to the cockpit with him. You buckle in next to him and prepare yourself for the crash. He aims for a clearing outside of the woods, but at the last second the second engine blows, and throws the aircraft off course. You end up landing in the forest and eventually skidding into a large lake. The front part of the aircraft is detached from the back during the crash, and it begins to fill with water. You are able to unbuckle yourself and leave the aircraft before you drown, but you realize the pilot is knocked out and unable to get himself out. There may not be time to get him out before you are permanently trapped underwater. You can choose to try to SAVE the pilot or EXIT the plane on your own. ")
        if third_level_scream_look.lower() == "save":
            print("You are able to unbuckle the pilot and pull him to safety just before the plane sinks to the bottom. You are rescued the next days and you are deemed a hero. You win the nobel peace prize for no reason, but you are so glad you chose to save the captain and bask in your new found fame.")
        elif third_level_scream_look.lower() == "exit":
            print("You are able to escape the plane, but the captain wakes up just before you exit due to the water hitting his face. He makes a face at you as if he can't believe you would leave him. You make it to safety and get rescued the next day, but you live the rest of eternity with regret and everybody ends up hating you because another passenger saw what you did and told everyone.")
        else:
            input("Not a valid option. Please choose SAVE or EXIT. ")
            if third_level_scream_look.lower() == "save":
                print("You are able to unbuckle the pilot and pull him to safety just before the plane sinks to the bottom. You are rescued the next days and you are deemed a hero. You win the nobel peace prize for no reason, but you are so glad you chose to save the captain and bask in your new found fame.")
            elif third_level_scream_look.lower() == "exit":
                print("You are able to escape the plane, but the captain wakes up just before you exit due to the water hitting his face. He makes a face at you as if he can't believe you would leave him. You make it to safety and get rescued the next day, but you live the rest of eternity with regret and everybody ends up hating you because another passenger saw what you did and told everyone.")
