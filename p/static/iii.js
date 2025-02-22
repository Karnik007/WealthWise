
let incomeTotal = 0;
let expenseTotal = 0;
let incomeSources = [];
let expenseSources = [];
const currentYear = new Date().getFullYear();
const currencyConfig = {
    default: 'INR',
    rates: {
        'INR': { symbol: '₹', rate: 1 },
        'USD': { symbol: '$', rate: 0.012 },
        'EUR': { symbol: '€', rate: 0.011 },
        'GBP': { symbol: '£', rate: 0.009 },
        'JPY': { symbol: '¥', rate: 1.6 }
    }
};

let currentCurrency = currencyConfig.default;
const incomeEmojis = [
    '💰', '💸', '💵', '💼', '🏠', '📈', '🤑', '💳', '🏦', '📊', '💲', '🧾'
];

const expenseEmojis = [
    '🍽', '🚗', '🏠', '📱', '🎓', '🛒', '💡', '🚌', '👗', '💊', '💇', '📚'
];
const currentMonth = new Date().getMonth();
function convertCurrency(amount, fromCurrency = 'INR', toCurrency = currentCurrency) {
    if (fromCurrency === toCurrency) return amount;
    
    const baseAmount = amount / currencyConfig.rates[fromCurrency].rate;
    return baseAmount * currencyConfig.rates[toCurrency].rate;
}
function initEmojiPickers() {
    const incomeEmojiPicker = document.querySelector('#addIncomeForm .emoji-picker');
    const expenseEmojiPicker = document.querySelector('#addExpenseForm .emoji-picker');

    // Populate Income Emoji Picker
    incomeEmojis.forEach(emoji => {
        const span = document.createElement('span');
        span.className = 'emoji-option';
        span.dataset.emoji = emoji;
        span.textContent = emoji;
        span.addEventListener('click', selectEmoji);
        incomeEmojiPicker.appendChild(span);
    });
    expenseEmojis.forEach(emoji => {
        const span = document.createElement('span');
        span.className = 'emoji-option';
        span.dataset.emoji = emoji;
        span.textContent = emoji;
        span.addEventListener('click', selectEmoji);
        expenseEmojiPicker.appendChild(span);
    });
    document.getElementById('month').value = currentMonth;
}
function initCurrencySelector() {
    const currencySelect = document.getElementById('currencySelector');
    currencySelect.innerHTML = ''; // Clear existing options

    Object.keys(currencyConfig.rates).forEach(currency => {
        const option = document.createElement('option');
        option.value = currency;
        option.textContent = `${currency} (${currencyConfig.rates[currency].symbol})`;
        currencySelect.appendChild(option);
    });

    currencySelect.value = currentCurrency;
    currencySelect.addEventListener('change', changeCurrency);
}
function selectEmoji(event) {
    const picker = event.target.closest('.emoji-picker');
    picker.querySelectorAll('.emoji-option').forEach(el => el.classList.remove('selected-emoji'));
    event.target.classList.add('selected-emoji');
    const hiddenInput = picker.querySelector('input[type="hidden"]');
    hiddenInput.value = event.target.dataset.emoji;
}
function changeCurrency(event) {
    const newCurrency = event.target.value;
    currentCurrency = newCurrency;
    incomeSources.forEach(source => {
        source.monthlyAmounts = source.monthlyAmounts.map(amount => 
            convertCurrency(amount, 'INR', newCurrency)
        );
    });
    expenseSources.forEach(source => {
        source.monthlyAmounts = source.monthlyAmounts.map(amount => 
            convertCurrency(amount, 'INR', newCurrency)
        );
    });
    renderIncomeSources();
    renderExpenseSources();
    updateTotals();
    updateCurrencySymbols();
}
function updateCurrencySymbols() {
    const currencySymbol = currencyConfig.rates[currentCurrency].symbol;
    document.querySelectorAll('.currency-symbol').forEach(el => {
        el.textContent = currencySymbol;
    });
}
function toggleForm(formId) {
    const incomeForm = document.getElementById('addIncomeForm');
    const expenseForm = document.getElementById('addExpenseForm');

    if (formId === 'addIncomeForm') {
        incomeForm.style.display = incomeForm.style.display === 'none' || incomeForm.style.display === '' ? 'block' : 'none';
        expenseForm.style.display = 'none';
    } else {
        expenseForm.style.display = expenseForm.style.display === 'none' || expenseForm.style.display === '' ? 'block' : 'none';
        incomeForm.style.display = 'none';
    }
}
function addIncome(event) {
    event.preventDefault();
    const name = event.target.name.value.trim();
    const amount = parseFloat(event.target.amount.value);
    const frequency = event.target.frequency.value;
    const emoji = document.getElementById('incomeEmoji').value;

    if (!name || isNaN(amount) || amount <= 0 || !emoji) {
        alert("Please fill in all details correctly.");
        return;
    }

    const incomeSource = {
        name,
        emoji,
        amount,
        frequency,
        monthlyAmounts: calculateMonthlyAmount(amount, frequency, currentMonth)
    };

    incomeSources.push(incomeSource);
    renderIncomeSources();
    updateTotals();
    event.target.reset();
    toggleForm('addIncomeForm');
}

function addExpense(event) {
    event.preventDefault();
    
    const name = event.target.name.value.trim();
    const amount = parseFloat(event.target.amount.value);
    const frequency = event.target.frequency.value;
    const emoji = document.getElementById('expenseEmoji').value;

    if (!name || isNaN(amount) || amount <= 0 || !emoji) {
        alert("Please fill in all details correctly.");
        return;
    }

    const expenseSource = {
        name,
        emoji,
        amount,
        frequency,
        monthlyAmounts: calculateMonthlyAmount(amount, frequency, currentMonth)
    };

    expenseSources.push(expenseSource);
    renderExpenseSources();
    updateTotals();
    event.target.reset();
    toggleForm('addExpenseForm');
}

function calculateMonthlyAmount(amount, frequency, startMonth) {
    const monthlyAmounts = Array(12).fill(0);
    
    switch(frequency) {
        case 'monthly':
            monthlyAmounts.fill(amount);
            break;
        case 'yearly':
            monthlyAmounts.fill(amount / 12);
            break;
        case 'one-time':
            monthlyAmounts[startMonth] = amount;
            break;
    }
    return monthlyAmounts;
}
function renderIncomeSources() {
    const incomeList = document.getElementById('incomeList');
    const currentMonthSelected = parseInt(document.getElementById('month').value);
    
    incomeList.innerHTML = '';

    incomeSources.forEach((source, index) => {
        const monthlyAmount = source.monthlyAmounts[currentMonthSelected];
        if (monthlyAmount > 0) {
            const sourceElement = document.createElement('div');
            sourceElement.className = 'category-item';
            sourceElement.innerHTML = `
                <div class="category-name">
                    <span class="category-icon">${source.emoji}</span>
                    <span>${source.name} (${source.frequency})</span>
                </div>
                <span><span class="currency-symbol">${currencyConfig.rates[currentCurrency].symbol}</span>${monthlyAmount.toFixed(2)}</span>
                <button class="delete-btn" onclick="deleteIncome(${index})">x</button>
            `;
            incomeList.appendChild(sourceElement);
        }
    });
}

// Render Expense Sources
function renderExpenseSources() {
    const expenseList = document.getElementById('expenseList');
    const currentMonthSelected = parseInt(document.getElementById('month').value);
    
    expenseList.innerHTML = '';

    expenseSources.forEach((source, index) => {
        const monthlyAmount = source.monthlyAmounts[currentMonthSelected];
        if (monthlyAmount > 0) {
            const sourceElement = document.createElement('div');
            sourceElement.className = 'category-item';
            sourceElement.innerHTML = `
                <div class="category-name">
                    <span class="category-icon">${source.emoji}</span>
                    <span>${source.name} (${source.frequency})</span>
                </div>
                <span><span class="currency-symbol">${currencyConfig.rates[currentCurrency].symbol}</span>${monthlyAmount.toFixed(2)}</span>
                <button class="delete-btn" onclick="deleteExpense(${index})">x</button>
            `;
            expenseList.appendChild(sourceElement);
        }
    });
}
function confirmDeletion(callback) {
    // Create a modal dynamically
    const modal = document.createElement('div');
    modal.className = 'deletion-modal';
    modal.innerHTML = `
        <div class="modal-content">
            <h3>Delete Confirmation</h3>
            <p>Choose deletion scope:</p>
            <div class="modal-buttons">
                <button onclick="handleDeletionChoice('current')">Current Month</button>
                <button onclick="handleDeletionChoice('future')">Current & Future Months</button>
                // <button class="red-button" onclick="handleDeletionChoice('all')">Entire Entry</button>
                <button onclick="closeDeletionModal()">Cancel</button>
            </div>
        </div>
    `;


    const style = document.createElement('style');
    style.innerHTML = `
        .red-button {
            background-color: red;
            color: white;
        }
        .deletion-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background: black;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .modal-buttons {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        .modal-buttons button {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            background-color: green;
            color: black;
        }
        .modal-buttons button:hover {
            opacity: 0.8;
        }
    `;
    document.head.appendChild(style);
    document.body.appendChild(modal);
    window.handleDeletionChoice = (scope) => {
        callback(scope);
        closeDeletionModal();
    };

    window.closeDeletionModal = () => {
        document.body.removeChild(modal);
    };
}
function deleteIncome(index) {
    confirmDeletion((scope) => {
        const currentMonthSelected = parseInt(document.getElementById('month').value);
        
        if (scope === 'current') {
            incomeSources[index].monthlyAmounts[currentMonthSelected] = 0;
        } else if (scope === 'future') {
            for (let i = currentMonthSelected; i < 12; i++) {
                incomeSources[index].monthlyAmounts[i] = 0;
            }
        } else if (scope === 'all') {
            incomeSources.splice(index, 1);
        }
        
        renderIncomeSources();
        updateTotals();
    });
}
function deleteExpense(index) {
    confirmDeletion((scope) => {
        const currentMonthSelected = parseInt(document.getElementById('month').value);
        
        if (scope === 'current') {
            expenseSources[index].monthlyAmounts[currentMonthSelected] = 0;
        } else if (scope === 'future') {
            for (let i = currentMonthSelected; i < 12; i++) {
                expenseSources[index].monthlyAmounts[i] = 0;
            }
        } else if (scope === 'all') {
            expenseSources.splice(index, 1);
        }
        
        renderExpenseSources();
        updateTotals();
    });
}
function updateTotals() {
    const currentMonthSelected = parseInt(document.getElementById('month').value);
    incomeTotal = incomeSources.reduce((total, source) => 
        total + source.monthlyAmounts[currentMonthSelected], 0);
    
    expenseTotal = expenseSources.reduce((total, source) => 
        total + source.monthlyAmounts[currentMonthSelected], 0);
    document.getElementById('totalIncome').innerText = `${currencyConfig.rates[currentCurrency].symbol}${incomeTotal.toFixed(2)}`;
    document.getElementById('totalExpenses').innerText = `${currencyConfig.rates[currentCurrency].symbol}${expenseTotal.toFixed(2)}`;
    const savings = incomeTotal - expenseTotal;
    document.getElementById('savings').innerText = `${currencyConfig.rates[currentCurrency].symbol}${savings.toFixed(2)}`;
    updateProgressBars(incomeTotal, expenseTotal, savings);
}
function updateProgressBars(income, expenses, savings) {
    const incomeBar = document.querySelector('.progress-bar.safe');
    const expenseBar = document.querySelector('.progress-bar.danger');
    const savingsBar = document.querySelector('.progress-bar.warning');
    const total = income > 0 ? income : 1;
    incomeBar.style.width = (income / total) * 100 + '%';
    expenseBar.style.width = (expenses / total) * 100 + '%';
    savingsBar.style.width = (savings / total) * 100 + '%';
}
document.getElementById('month').addEventListener('change', () => {
    renderIncomeSources();
    renderExpenseSources();
    updateTotals();
});

document.addEventListener('DOMContentLoaded', () => {
    initEmojiPickers();
    initCurrencySelector();
    document.getElementById('addIncomeForm').addEventListener('submit', addIncome);
    document.getElementById('addExpenseForm').addEventListener('submit', addExpense);
    updateTotals();addExpense
    updateCurrencySymbols();
});