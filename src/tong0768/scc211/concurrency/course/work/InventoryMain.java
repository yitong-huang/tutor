package tong0768.scc211.concurrency.course.work;

import java.util.concurrent.CountDownLatch;

/**
 * @author tong0768
 */
public class InventoryMain {

    public static void main(String[] args) throws InterruptedException {

        if (args == null || args.length != 2) {
            System.out.println("invalid args num");
            return;
        }

        int addThreadNum = 0;
        int removeThreadNum = 0;

        try {
            addThreadNum = Integer.parseInt(args[0]);
            removeThreadNum = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
            System.out.println("not a valid number");
        }

        CountDownLatch latch = new CountDownLatch(addThreadNum + removeThreadNum);
        Warehouse warehouse = new WarehouseSafe(latch);

//        Warehouse warehouse = new WarehouseUnsafe();

        for (int i = 0; i < addThreadNum; i++) {
            new AddThread(warehouse).start();

        }

        for (int i = 0; i < removeThreadNum; i++) {
            new RemoveThread(warehouse).start();
        }

        latch.await();

//        TimeUnit.SECONDS.sleep(1);
        System.out.println("Final Inventory size = " + warehouse.getInventorySize());

    }

}




