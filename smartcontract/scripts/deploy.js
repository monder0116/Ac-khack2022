async function main() {

  const Transactions = await hre.ethers.getContractFactory("Transactions");
  const example = await Transactions.deploy();

  await example.deployed();

  console.log("Greeter deployed to:", example.address);
}


const runMain= async()=>{
  try {
      await main();
      process.exit(0);
  } catch (error) {
    console.log(error);
    process.exit(1);
  }
}

runMain();
