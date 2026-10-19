from blockchain import Blockchain
from query import Query


def print_block(block):
    """打印区块信息"""
    print("-" * 40)
    print(f"区块高度：{block.height}")
    print(f"区块数据：{block.data}")
    print(f"时间戳：{block.timestamp}")
    print(f"前置哈希：{block.prev_hash}")
    print(f"当前哈希：{block.hash}")
    print("-" * 40)


def print_menu():
    """打印命令行菜单"""
    print("\n========== MiniBLC 区块链系统 ==========")
    print("1. 添加区块")
    print("2. 根据高度查询区块")
    print("3. 查看整个区块链")
    print("4. 验证区块链")
    print("0. 退出系统")
    print("========================================")


def main():
    blockchain = Blockchain()
    query = Query(blockchain)

    while True:
        print_menu()
        choice = input("请输入操作编号：").strip()

        if choice == "1":
            data = input("请输入区块数据：").strip()

            if not data:
                print("区块数据不能为空！")
                continue

            blockchain.add_block_to_chain(data)
            print("区块添加成功！")
            print_block(blockchain.get_latest_block())

        elif choice == "2":
            try:
                height = int(input("请输入区块高度："))

                block = query.query_block_by_height(height)

                if block is None:
                    print("未找到该高度的区块！")
                else:
                    print_block(block)

            except ValueError:
                print("输入错误，请输入整数高度！")

        elif choice == "3":
            print("\n========== 区块链完整信息 ==========")

            for block in blockchain.chain:
                print_block(block)

            print(f"当前区块数量：{query.get_chain_nums()}")
            print(f"当前区块高度：{query.get_chain_height()}")

        elif choice == "4":
            print("\n正在验证区块链...")
            if blockchain.validate_chain():
                print("验证通过：区块链合法！")
            else:
                print("验证失败：区块链存在异常！")

        elif choice == "0":
            print("感谢使用 MiniBLC，再见！")
            break

        else:
            print("无效的操作编号，请重新输入！")


if __name__ == "__main__":
    main()