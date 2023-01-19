/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
class MyHashSet {
    List<Integer> hash;

    public MyHashSet() {
        hash = new ArrayList();
    }
    
    public void add(int key) {
        if(!hash.contains(key))
            hash.add(key);
    }
    
    public void remove(int key) {
        hash.remove(Integer.valueOf(key));
    }
    
    public boolean contains(int key) {
        return hash.contains(key);
    }
}
