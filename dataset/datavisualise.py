import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set a pleasant light theme with white grid and pastel colors.
sns.set_theme(style="whitegrid", palette="pastel")

# Set the path to your dataset folder (update this path as needed)
base_dir = r"C:\Users\Divyansh\OneDrive\Desktop\FinalDR\dataset"

# Define the subdirectories (splits) and categories (make sure names match your folders)
splits = ["train", "test", "validate"]
categories = ["normal", "mild", "moderate", "severe", "proliferative"]

def count_image_files(directory):
    """
    Count image files in a directory based on common image file extensions.
    """
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
    return sum(
        f.lower().endswith(valid_extensions)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    )

# Initialize dictionaries for overall counts and per-split counts
overall_category_counts = {cat: 0 for cat in categories}
split_category_counts = {split: {} for split in splits}

# Traverse through each split and category folder to count images
for split in splits:
    for cat in categories:
        folder_path = os.path.join(base_dir, split, cat)
        if os.path.exists(folder_path):
            count = count_image_files(folder_path)
            overall_category_counts[cat] += count
            split_category_counts[split][cat] = count
        else:
            print(f"Warning: Folder not found: {folder_path}")

# Print overall counts to the console
print("Overall image counts per category:")
for cat, count in overall_category_counts.items():
    print(f"{cat}: {count}")
total_images = sum(overall_category_counts.values())
print(f"\nTotal number of images: {total_images}")

# -----------------------
# Plot 1: Normal vs Abnormal
# -----------------------
# "Normal" is as-is; "Abnormal" is the sum of all categories except "normal"
normal_count = overall_category_counts.get("normal", 0)
abnormal_count = total_images - normal_count

# Data for normal vs abnormal plot
labels = ["Normal", "Abnormal"]
counts = [normal_count, abnormal_count]

# Define a custom palette for this plot: a pleasant blue and light pink.
custom_palette = ["#AEC6CF", "#FFB6C1"]

plt.figure(figsize=(8, 6))
barplot1 = sns.barplot(x=labels, y=counts, palette=custom_palette)
plt.title("Normal vs Abnormal Image Distribution")
plt.xlabel("Type")
plt.ylabel("Number of Images")

# Annotate bars with counts
for i, count in enumerate(counts):
    plt.text(i, count + 0.01 * total_images, str(count), ha='center', va='bottom', fontweight='bold')
plt.show()

# -----------------------
# Plot 2: Distribution across Train, Test, Validate for Each Category
# -----------------------
# Prepare data for a grouped bar plot
rows = []
for split in splits:
    for cat in categories:
        count = split_category_counts[split].get(cat, 0)
        rows.append({"Split": split.capitalize(), "Category": cat.capitalize(), "Count": count})
df = pd.DataFrame(rows)

plt.figure(figsize=(10, 6))
# Create a grouped bar plot: x-axis is Category, hue for Split
barplot2 = sns.barplot(x="Category", y="Count", hue="Split", data=df)
plt.title("Dataset Distribution Across Splits for Each Category")
plt.xlabel("Category")
plt.ylabel("Number of Images")

# Annotate each bar with its count
for p in barplot2.patches:
    height = p.get_height()
    if height > 0:
        barplot2.annotate(format(int(height), 'd'),
                          (p.get_x() + p.get_width() / 2., height),
                          ha='center', va='bottom',
                          fontsize=9, color='black', fontweight='bold')
plt.legend(title="Dataset Split")
plt.show()




# import os
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Set the path to your dataset folder (update this path as needed)
# base_dir = "C:\\Users\\Divyansh\\OneDrive\\Desktop\\FinalDR\dataset"  # e.g., "/kaggle/input/your-dataset-folderdataset"

# # Define the subdirectories (splits) and categories (as per your directory structure)
# splits = ["train", "test", "validate"]
# categories = ["normal", "mild", "moderate", "severe", "proliferative"]

# def count_image_files(directory):
#     """
#     Count image files in a directory based on common image file extensions.
#     """
#     valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
#     return sum(
#         f.lower().endswith(valid_extensions)
#         for f in os.listdir(directory)
#         if os.path.isfile(os.path.join(directory, f))
#     )

# # Dictionary to store the cumulative image count per category across splits
# category_counts = {cat: 0 for cat in categories}

# # Traverse through each split and category folder to count images
# for split in splits:
#     for cat in categories:
#         folder_path = os.path.join(base_dir, split, cat)
#         if os.path.exists(folder_path):
#             count = count_image_files(folder_path)
#             category_counts[cat] += count
#         else:
#             print(f"Warning: Folder not found: {folder_path}")

# # Display the counts in the console
# print("Image counts per category:")
# for cat, count in category_counts.items():
#     print(f"{cat}: {count}")
# total_images = sum(category_counts.values())
# print(f"\nTotal number of images: {total_images}")

# # Plot the counts using seaborn and matplotlib
# plt.figure(figsize=(10, 6))
# sns.barplot(x=list(category_counts.keys()), y=list(category_counts.values()), color="skyblue")
# plt.title("Distribution of Images Across Categories")
# plt.xlabel("Categories")
# plt.ylabel("Number of Images")

# # Annotate each bar with its count value
# for i, (cat, count) in enumerate(category_counts.items()):
#     plt.text(i, count + 0.01 * total_images, str(count), ha='center', va='bottom', fontweight='bold')

# plt.show()


# # import os

# # # Path to your top-level dataset folder
# # base_dir = "C:\\Users\\Divyansh\\OneDrive\\Desktop\\FinalDR\dataset"

# # # Subfolders within the dataset directory
# # splits = ["train", "test", "validate"]

# # # Categories inside each split
# # categories = ["normal", "mild", "moderate", "severe", "proliferate"]

# # def count_image_files(directory):
# #     """
# #     Counts files in 'directory' that have common image extensions.
# #     Adjust or extend the valid_extensions tuple as needed.
# #     """
# #     valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
# #     return sum(f.lower().endswith(valid_extensions) for f in os.listdir(directory))

# # # Dictionary to keep track of total images per category (across all splits)
# # category_counts = {cat: 0 for cat in categories}

# # # Traverse each split and category folder to count images
# # for split in splits:
# #     for cat in categories:
# #         folder_path = os.path.join(base_dir, split, cat)
# #         if os.path.exists(folder_path):
# #             category_counts[cat] += count_image_files(folder_path)
# #         else:
# #             print(f"Warning: Folder not found: {folder_path}")

# # # Print the total images for each category
# # print("Images per category (across train, test, validate):")
# # for cat, count in category_counts.items():
# #     print(f"{cat}: {count}")

# # # Print the overall total
# # total_images = sum(category_counts.values())
# # print(f"\nTotal number of images across all categories and splits: {total_images}")
