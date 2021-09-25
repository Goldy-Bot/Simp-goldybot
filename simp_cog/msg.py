class footer():
    type_1 = "❗ To stop being simpable, type '!simpable off'."

class simpable():
    their_not_simpable = "**💛 {}, their not simpable!**"

    toggle_on = "**💚 {}, member's are now able to expose you for simping. (Warning: You will be pinged, many times. 😉)**"
    toggle_off = "**💛 {}, no one can expose you for simping now. Good choice, this is the safer option.**"

    your_not_simpable = "**💙 {}, don't worry you aren't simpable. *If for some reason you want to allow members to expose you, try this command --> ``!simpable on``.***"
    your_simpable = "**💛 {}, yes you are in deed simpable. *To stop members from exposing you, try this command --> ``!simpable off``.***"

class simp():
    class failed():
        not_simpable = simpable.their_not_simpable

    class embed():
        dm_context = """
        **YOUR A SIMP!!!**
        **STOP SIMPING!!!**
        """

        guild_context = """
        **EXPOSED, {} IS A SIMP!!!**
        **EXPOSED, {} IS A SIMP!!!**
        **EXPOSED, {} IS A SIMP!!!**
        """
