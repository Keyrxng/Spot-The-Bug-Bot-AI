pragma solidity ^8.0.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Test is Ownable {

    function withdraw() external onlyOwner {
        uint256 amount = payableToken.balanceOf(address(this));
        payable.transferFrom(address(this), msg.sender, amount);
        emit NewWithdrawal(msg.sender, amount);
    }
}