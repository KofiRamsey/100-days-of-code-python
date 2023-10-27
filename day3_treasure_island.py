print('''
*******************************************************************************
                             . . . .
                                ,`,`,`,`,
          . . . .               `\`\`\`\;
          `\`\`\`\`,            ~|;!;!;\!
           ~\;\;\;\|\          (--,!!!~`!       .
          (--,\\\===~\         (--,|||~`!     ./
           (--,\\\===~\         `,-,~,=,:. _,//
            (--,\\\==~`\        ~-=~-.---|\;/J,
             (--,\\\((```==.    ~'`~/       a |
               (-,.\\('('(`\\.  ~'=~|     \_.  \
                  (,--(,(,(,'\\. ~'=|       \\_;>
                    (,-( ,(,(,;\\ ~=/        \
                    (,-/ (.(.(,;\\,/          )
                     (,--/,;,;,;,\\         ./------.
                       (==,-;-'`;'         /_,----`. \
               ,.--_,__.-'                    `--.  ` \
              (='~-_,--/        ,       ,!,___--. \  \_)
             (-/~(     |         \   ,_-         | ) /_|
             (~/((\    )\._,      |-'         _,/ /
              \\))))  /   ./~.    |           \_\;          
           ,__/////  /   /    )  /
            '===~'   |  |    (, <.
                     / /       \. \
                   _/ /          \_\
                  /_!/            >_\


*******************************************************************************
''')
print("WELCOME TO TREASURE ISLAND.")
print("YOUR MISSION IS TO FIND THE UNICORN.")

choice1 = input('You are at a fork in the path. Do you want to go "left" or "right"? ').lower()
if choice1 == "right":
    print("You walked into a trap! Game Over.")
elif choice1 == "left":
    choice2 = input('You\'ve reached a river. Do you want to "swim" across or "wait" for a bridge to appear? ').lower()
    if choice2 == "swim":
        print("You were caught by a whirlpool! Game Over.")
    elif choice2 == "wait":
        choice3 = input(
            "A magical bridge appears and you cross to the other side. There are three doors ahead. One red, one blue, and one yellow. Which one do you choose? ").lower()
        if choice3 == "red":
            print("The door leads to a dragon's lair! Game Over.")
        elif choice3 == "blue":
            print("You are frozen by an ice spell! Game Over.")
        elif choice3 == "yellow":
            print("You have found the magical unicorn! Congratulations, You Won!")
        else:
            print("That door doesn't exist! Game Over.")
    else:
        print("Invalid choice! Game Over.")
else:
    print("Invalid choice! Game Over.")
