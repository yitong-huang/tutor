package tong0768.operation.scc211.concurrency.course.work;

public class RemoveThread extends Thread {

    private final Warehouse warehouse;

    public RemoveThread(Warehouse warehouse) {
        this.warehouse = warehouse;
    }

    @Override
    public void run() {
        warehouse.remove();
    }
}
