# Pixela_Habit_Tracker
---

# 📈 Pixela Coding Activity Tracker

This Python script allows you to track your daily coding time using the [Pixela](https://pixe.la) graphing service. The script prompts the user to input the number of minutes coded today, then sends that data to a Pixela graph. It automatically detects the current date in the **Pacific/Auckland** timezone.

## 🔧 Features

- Create a Pixela user and graph (commented out by default)
- Log your daily coding activity in minutes
- Automatically formats today's date for Pixela
- Sends a POST request to add data to your graph

## 🧰 Requirements

- Python 3.x
- `requests` library
- `pytz` library

Install the required packages if you haven't already:

```bash
pip install requests pytz
```

## 📜 Usage

1. **Configure your user and token:**

   Replace the following variables with your own Pixela credentials:

   ```python
   token = "YOUR_PIXELA_TOKEN"
   username = "YOUR_PIXELA_USERNAME"
   ```

2. **Run the script:**

   ```bash
   python pixela_tracker.py
   ```

   You'll be prompted:

   ```
   How many minutes did you code today?
   ```

   Enter your answer, and it will be logged to your graph for today.

3. **Check your graph:**

   Visit: `https://pixe.la/v1/users/YOUR_USERNAME/graphs/graph1.html`

## 🗃️ Optional Endpoints (Commented in Code)

- **User creation:** The script includes parameters for creating a new Pixela user account.
- **Graph creation:** You can uncomment the relevant section to create a new graph.
- **Update/Delete entries:** Code snippets are provided to update or delete today's entry.

## 📝 Notes

- The graph ID used is `"graph1"`, and the unit is `"minutes"`.
- Date is automatically set using the **Pacific/Auckland** timezone.
- Colors and graph settings are customizable via the `graph_config` dictionary.

## 📌 References

- [Pixela API Documentation](https://docs.pixe.la/)

---
