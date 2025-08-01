# Portfolio Value Tracker - Interview Coding Exercise

## Objective
Create a portfolio value tracker that monitors the total USD value of assets for a specific wallet address and logs the value every 5 seconds.

## Advice

Take your time reading through the prompt, ask questions to clarify and digest the problem, and use provided links and documentation to help you as needed. 

It is OK if you don't understand all or some of the task - this problem is not solely for judging web3/crypto knowledge and coding abilities, but also to test one's ability to read documentation, identify and map out the important details of a (potentially unfamiliar) problem, and ask good clarifying questions.

## Task Requirements

### 1. Track Assets
Monitor the following assets for the user `0x9B974aF13ae64775E7E96fd92d9089b479cB57C5`:
- **ETH** - Native Base network token
- **USDC** - Address = `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`
- **Metamorpho Spark USDC** - Address = `0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A`
    - Vault UI: [https://app.morpho.org/base/vault/0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A/spark-usdc-vault](https://app.morpho.org/base/vault/0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A/spark-usdc-vault)

### 2. Calculate Portfolio Value
- Sum value of each position to calculate total portfolio value

### 3. Price Data
You can connect to August price API to get token prices by symbol: `https://prices.augustdigital.io/price/{symbol}`

### 4. Logging Requirements
- Log the portfolio value every 5 seconds
- Include any checks or error handling logic as you see fit

### 5. Sanity Check
Use Debank to sanity check your calculated portfolio value.
- [https://debank.com/profile/0x9B974aF13ae64775E7E96fd92d9089b479cB57C5](https://debank.com/profile/0x9B974aF13ae64775E7E96fd92d9089b479cB57C5)

## File structure
The project includes:
- `main.py` - Main script with some Web3 / contract boilerplate (write your code here)
- `ierc20_abi.json` - ERC20 token ABI for standard token interactions
- `ierc4626_abi.json` - ERC4626 vault ABI for Metamorpho interactions
- `requirements.txt` - Dependencies file

## Technical Notes
- Helpful comments with doc links are in `main.py`
- Use the provided ABIs for contract interactions
- Also you can use block explorers (basescan.org) to help find relevant contract functions
- Please disable AI/LLM assistance while working through this problem.

## TL;DR
1. Clone this repo and install dependencies to get started.
1. Implement the portfolio calculation logic in `main()` in a 5-second loop.
3. Verify your implementation against Debank.

Good luck!
Feel free to ask me questions!
