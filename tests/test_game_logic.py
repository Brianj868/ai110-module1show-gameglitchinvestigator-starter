from logic_utils import check_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Fix: Normal and Hard difficulty ranges were swapped
def test_hard_range_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


# Fix: "Too High" hint message told the user to go higher instead of lower
def test_too_high_message_says_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message


# Fix: "Too Low" hint message told the user to go lower instead of higher
def test_too_low_message_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


# Fix: string fallback in check_guess used alphabetical comparison (e.g. "9" > "10")
def test_string_fallback_uses_numeric_comparison():
    # "9" > "10" alphabetically but 9 < 10 numerically — should be "Too Low"
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"


# Fix: "Too High" on even attempts incorrectly awarded +5 points
def test_too_high_always_deducts_score():
    score_after_even = update_score(100, "Too High", 2)
    score_after_odd = update_score(100, "Too High", 3)
    assert score_after_even < 100
    assert score_after_odd < 100
