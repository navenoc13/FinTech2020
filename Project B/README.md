# Project B - Smart Contract
 Based on the class, everyone should understand that the "coin" or "token" is basically a smart contract on Ethereum blockchain. In this assignment, you will be learning ERC20 protocol by hand-on writing your own smart contract.
Please follow the ERC20 protocol below and launch your own token contract on "Ropsten" Ethereum testnet:

1. function totalSupply() public constant returns (uint);
2. function balanceOf(address tokenOwner) public constant returns (uint balance);
3. function allowance(address tokenOwner, address spender) public constant returns (uint remaining);
4. function transfer(address to, uint tokens) public returns (bool success);
5. function approve(address spender, uint tokens) public returns (bool success);
6. function transferFrom(address from, address to, uint tokens) public returns (bool success);

7. event Transfer(address indexed from, address indexed to, uint tokens);
8. event Approval(address indexed tokenOwner, address indexed spender, uint tokens);


Please name your token after you student ID and send it to the address 0xd2448AC204465aB30e20652421FA70B5DaF8Dd15. After sending the token to specified address, please hand in a document which contains: 1. Your code, 2. The address of contract, 3. screenshot of transaction on Etherscan, to ceiba (in PDF).
