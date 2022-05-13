//https://eth-ropsten.alchemyapi.io/v2/vVcL_UWUplyAfIUfvAqLjgr0es1fqgBY
require('@nomiclabs/hardhat-waffle');
module.exports = {
  solidity: '0.8.0',
  networks: {
    ropsten: {
      url: 'https://eth-ropsten.alchemyapi.io/v2/vVcL_UWUplyAfIUfvAqLjgr0es1fqgBY',
      accounts: ['fc9a25e653db70008cc3703e912a484d4ac5f72310cc582037d6a19fc983e122'],
    },
  },
};