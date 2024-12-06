from filler_to_newtext import load_ipadic_dict
from do_parsing import dependency_analysis_with_syntax_tree
#from command_creation_module import create_command

def process_root_and_generate_commands(root):
    for phrase in root:
        verb = phrase[0].word
        verb_pos = phrase[0].pos
        dependents = []
        dependents_pos = []
        for child in phrase[0].children:
            dependents.append(child.word)
            dependents_pos.append(child.pos) 
            print(f"dependents: {child.word}({child.pos})")
        
        
        print(f"Processing verb: {verb} ({verb_pos})")
        


# メイン実行部分
if __name__ == "__main__":
    ipadic_dir_path = "/home/rf22127/mecab/mecab-ipadic-2.7.0-20070801/"

    # load_ipadic_dict：辞書を読み込む
    dictionary = load_ipadic_dict(ipadic_dir_path)

    text = "その場で右に回る前に速度を落として後ろに進んで"
    root = dependency_analysis_with_syntax_tree(text, dictionary)
    # 構文木の出力
    print("\n返ってくる構文:")
    print(root)
    
    process_root_and_generate_commands(root)