from blockchain import Blockchain


def main():
    print()
    blockchain = Blockchain()
    print(blockchain.chain)
    print()
    for i in range(1, 10):
        data = {
            'name': 'Mining Block {}'.format(i),
        }
        blockchain.add_new_data(data)
        blockchain.mine()
        blockchain.difficulty += 1
        print()
    print(blockchain.chain)


if __name__ == "__main__":
    main()
