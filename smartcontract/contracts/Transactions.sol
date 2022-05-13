//SPDX-License-Identifier: UNLICENSED

pragma solidity^0.8.0;
contract Transactions{
    
uint256 transactionCount;
TransferStruct[] arr;
event Transfer(address from, address rec, string designdata,uint amount, uint256 timestamp);

struct TransferStruct{
    address from;
    address rec;
    uint amount;
    string designdata;
    uint256 timestamp;

}
function add2blockchain(address payable receiver, uint amount, string memory  designdata )public {
    transactionCount += 1;
    arr.push(TransferStruct(msg.sender,receiver,amount,designdata,block.timestamp));
    emit Transfer(msg.sender,receiver,designdata,amount,block.timestamp);
}
function getAllTransactions()public view returns(TransferStruct[] memory) {
    return arr;
}
function getTotalCount()public view returns(uint256 ) {
    return transactionCount;
}
}


