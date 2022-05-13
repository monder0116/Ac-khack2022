//SPDX-License-Identifier: UNLICENSED

pragma solidity^0.8.0;
contract Transaction{

uint256 transactionCount;

event Transfer(address from, address rec, string designdata,uint amount, uint256 timestamp);


struct TransferStruct{
    address from;
    address rec;
    uint amount;
    string designdata;
    uint256 timestamp;

}
TransferStruct[] arr;
function add2blockchain(address payable receiver, uint amount, string memory message, string memory account, string memory keyword)public {
     transactionCount += 1;
}
function getAllTransactions()public view returns(TransferStruct[] memory) {
    
}
function getTotalCount()public view returns(uint256 ) {
    
}
}


