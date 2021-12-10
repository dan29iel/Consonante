def main():
    state = "Practica els problemes de list comprehnsion sper a ser Pythonic!"

    consonants = [i for i in state if i not in 'AaEeIiOoUu']

    print(consonants)

if __name__ == '__main__':
    main()
