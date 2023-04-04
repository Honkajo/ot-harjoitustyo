import pytest
from unittest.mock import patch
from WalletTracker import Budget

@patch('builtins.input', side_effect=['2', '50', 'Test expense', '2022-01-02', '0'])
def test_add_expense(mock_input):
    budget = Budget()
    budget.run_menu()
    assert budget.get_balance() == -50













