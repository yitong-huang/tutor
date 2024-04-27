package tong0768.concurrency;

import java.util.concurrent.CountDownLatch;

public class WarehouseSafe implements Warehouse {

    private int inventorySize = 0;
    private CountDownLatch latch;

    public WarehouseSafe(CountDownLatch latch) {
        this.latch = latch;
    }

    @Override
    public synchronized void add() {
        inventorySize += 1;
        System.out.println("Added. Inventory size = " + inventorySize);
        latch.countDown();
    }

    @Override
    public synchronized void remove() {
        inventorySize -= 1;
        System.out.println("Removed. Inventory size = " + inventorySize);
        latch.countDown();
    }

    @Override
    public synchronized int getInventorySize() {
        return inventorySize;
    }
}
