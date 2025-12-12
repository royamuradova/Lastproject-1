from schedule import Schedule

filename = "courses_2023.csv"

bst_schedule = Schedule(use_avl=False)
avl_schedule = Schedule(use_avl=True)

print("Loading CSV into BST and AVL...")
bst_schedule.load_from_csv(filename)
avl_schedule.load_from_csv(filename)
print("Loaded successfully!\n")

print("BST height =", bst_schedule.tree_height())
print("AVL height =", avl_schedule.tree_height())
