#_________________________________________________________
# Setters n Getters
'''
Getter: Retrieves a value.
Setter: Changes a value, optionally checking whether the new value is valid.
'''
#---------------------------------------------------------

'''Python has a built-in decorator called @property. 
   It works exactly like the 3-layered decorators you just built, but Python handles the layers for you! '''

class Player:
    def __init__(self):
        # The underscore means "Hey, treat this as a private variable!"
        self._health = 100 

    # 1. THE GETTER (Reads the value)
    @property
    def health(self):
        print("🔍 Intercepted! Someone is reading the health value.")
        return self._health

    # 2. THE SETTER (Writes/Validates the value)
    @health.setter
    def health(self, new_value):
        print(f"🛡️ Intercepted! Someone wants to change health to: {new_value}")
        
        # Look familiar? Your Level 1 Gatekeeper logic!
        if new_value < 0:
            print("❌ Guard: Health cannot be negative. Clamping to 0.")
            self._health = 0
        else:
            self._health = new_value




#

# class myClass:
#     def __init__(self, value):
#         self._value = value
