// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor (uint256 initialSupply_) ERC20("Token","TKN"){
        _mint(msg.sender, initialSupply_);
    }

    function burn(uint256 _amount) public {
        _burn(msg.sender, _amount);
    }
}