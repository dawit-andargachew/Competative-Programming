//https://www.youtube.com/watch?v=xpSfcHDTPZQ
class LRUCache {

    Node head =  new Node(0,0);
    Node tail =  new Node(0,0);
    HashMap<Integer,Node> map = new HashMap();
    int capacity;

    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;        
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            Node node = map.get(key);
            remove(node);
            insert(node);
            return node.value;
        }
        return -1;        
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key))
            remove(map.get(key));

        else if(map.size() == capacity)
                remove(tail.prev);

        insert(new Node(key,value));
    }
    
    void remove(Node node){
        map.remove(node.key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    void insert(Node node){
        map.put(node.key, node);
        Node headN = head.next;
        head.next = node;
        node.prev = head;
        headN.prev = node;
        node.next = headN;
    }

    class Node{
        Node prev, next;
        int key,value;
        Node(int k, int v){
            key = k;
            value = v;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */


//  public class LRUCache {
//     Stack <Integer> K;
//     Stack <Integer> V;
//     int capacity;

//     public LRUCache(int capacity) {
//         K = new Stack();
//         V = new Stack();
//         this.capacity = capacity;
//     }
    
//     public int get(int key) {
//         if(!K.contains(key))
//             return -1;
        
//         int index = K.indexOf(key);
//         int value = V.get(index);

//         K.remove(index);// remove the actual object
//         V.remove(index);// remov by index

//         K.add(key);
//         V.add(value);
//         return value;  
//     }
    
//     public void put(int key, int value) {
//          if(K.contains(key)){
//              int index = K.indexOf(key);
//              K.remove(index);
//              V.remove(index);

//              K.push(key);
//              V.push(value);
//             }
//        else { 
//             if(K.size() == capacity){
//                 K.remove(0);
//                 V.remove(0);
//             }

//             K.push(key);
//             V.push(value);
//         }
//     }
// }


