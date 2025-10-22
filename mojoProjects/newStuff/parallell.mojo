from algorithm import parallelize

fn step(k: Int) capturing -> None:
    print(k)

def main():
    parallelize[step](num_work_items=10, num_workers=10)