package operation.scc211.concurrency.course.work;

@SuppressWarnings("unused")
public class WarehouseUnsafe implements Warehouse {

    private int inventorySize = 0;

    @Override
    public void add() {
        inventorySize += 1;
        System.out.println("Added. Inventory size = " + inventorySize);
    }

    @Override
    public void remove() {
        inventorySize -= 1;
        System.out.println("Removed. Inventory size = " + inventorySize);
    }

    @Override
    public int getInventorySize() {
        return inventorySize;
    }
}
