def interpret(self, command: str) -> str:
        final = ""
        for i in range(len(command)):
            if command[i] == 'G':
                final+='G'
            elif command[i] == '(':
                if(command[i+1] == ')'):
                    final+='o'
                elif command[i+1] == 'a':
                    final+='al'
        return final
