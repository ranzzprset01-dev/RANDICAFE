/**
 * RANDI CAFE - Core Application & Real-time State
 * Manages menus, cart, order submission, admin authentication, and cross-tab/cloud sync.
 */

// 1. Initial Menu Data (High-definition Unsplash photos, categorized, curated prices)
const DEFAULT_MENUS = [
  // COFFEE
  {
    id: 1,
    name: "Espresso Doppio",
    category: "Coffee",
    price: 22000,
    desc: "Ekstraksi ganda biji arabika pilihan dengan crema tebal dan aroma intens.",
    image: "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?auto=format&fit=crop&w=600&q=80",
    badge: "Signature",
    available: true
  },
  {
    id: 2,
    name: "Kopi Susu Gula Aren",
    category: "Coffee",
    price: 25000,
    desc: "Espresso house blend dipadu susu segar creamy dan sirup gula aren organik.",
    image: "https://images.unsplash.com/photo-1541167760496-1628856ab772?auto=format&fit=crop&w=600&q=80",
    badge: "Popular",
    available: true
  },
  {
    id: 3,
    name: "Caramel Macchiato",
    category: "Coffee",
    price: 32000,
    desc: "Vanilla steamed milk dengan layer espresso pekat dan drizzle karamel gurih.",
    image: "https://images.unsplash.com/photo-1485808191679-5f86510681a2?auto=format&fit=crop&w=600&q=80",
    badge: "Popular",
    available: true
  },
  {
    id: 4,
    name: "Spanish Latte",
    category: "Coffee",
    price: 30000,
    desc: "Latte khas dengan sentuhan kental manis berkualitas untuk rasa manis pas.",
    image: "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=600&q=80",
    badge: "New",
    available: true
  },
  {
    id: 5,
    name: "Cold Brew Black",
    category: "Coffee",
    price: 28000,
    desc: "Seduhan dingin 16 jam dengan rasa buah ringan, minim asam, dan sangat menyegarkan.",
    image: "https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?auto=format&fit=crop&w=600&q=80",
    badge: "",
    available: true
  },

  // NON-COFFEE
  {
    id: 6,
    name: "Kyoto Matcha Latte",
    category: "Non-Coffee",
    price: 30000,
    desc: "Pure ceremonial grade green tea matcha dari Uji dipadu susu oat lembut.",
    image: "https://images.unsplash.com/photo-1536256263959-770b48d82b0a?auto=format&fit=crop&w=600&q=80",
    badge: "Popular",
    available: true
  },
  {
    id: 7,
    name: "Dark Chocolate Signature",
    category: "Non-Coffee",
    price: 28000,
    desc: "Kakao premium Belgia 70% dengan susu segar hangat atau dingin yang kaya rasa.",
    image: "https://images.unsplash.com/photo-1542990253-0d0f5be5f0ed?auto=format&fit=crop&w=600&q=80",
    badge: "Signature",
    available: true
  },
  {
    id: 8,
    name: "Red Velvet Velvetine",
    category: "Non-Coffee",
    price: 29000,
    desc: "Kombinasi klasik red velvet dengan hint keju lembut dan foam gurih.",
    image: "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=600&q=80",
    badge: "",
    available: true
  },

  // SIGNATURE COLD & TEA
  {
    id: 9,
    name: "Lychee Blossom Tea",
    category: "Tea & Mocktail",
    price: 24000,
    desc: "Seduhan teh hitam melati berpadu buah leci utuh dan mint aromatik.",
    image: "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=600&q=80",
    badge: "Popular",
    available: true
  },
  {
    id: 10,
    name: "Sunset Berry Mocktail",
    category: "Tea & Mocktail",
    price: 28000,
    desc: "Bulir strawberry segar, soda sparkling, dan hint lemon segar berlapis warna cantik.",
    image: "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=600&q=80",
    badge: "Signature",
    available: true
  },

  // MAIN COURSE & PASTA
  {
    id: 11,
    name: "Nasi Goreng Wagyu Randi",
    category: "Main Course",
    price: 45000,
    desc: "Nasi goreng bumbu rempah nusantara dengan potongan daging wagyu empuk dan telur mata sapi.",
    image: "https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=600&q=80",
    badge: "Signature",
    available: true
  },
  {
    id: 12,
    name: "Spaghetti Creamy Carbonara",
    category: "Main Course",
    price: 38000,
    desc: "Pasta al dente dengan saus keju parmesan asli, smoked beef renyah, dan egg yolk.",
    image: "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=600&q=80",
    badge: "Popular",
    available: true
  },
  {
    id: 13,
    name: "Chicken Katsu Curry Rice",
    category: "Main Course",
    price: 39000,
    desc: "Fillet ayam goreng tepung renyah dengan siraman saus kari Jepang kental dan sayuran.",
    image: "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=600&q=80",
    badge: "",
    available: true
  },

  // SNACKS & DESSERTS
  {
    id: 14,
    name: "Truffle Parmesan Fries",
    category: "Snack",
    price: 26000,
    desc: "Kentang goreng renyah wangi minyak truffle murni ditaburi keju parmesan gurih.",
    image: "https://images.unsplash.com/photo-1576107232684-1279f3908594?auto=format&fit=crop&w=600&q=80",
    badge: "Popular",
    available: true
  },
  {
    id: 15,
    name: "Croissant Almond Butter",
    category: "Snack",
    price: 28000,
    desc: "Pastry renyah berlapis butter prancis dengan isian krim almond manis.",
    image: "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=80",
    badge: "Signature",
    available: true
  },
  {
    id: 16,
    name: "Cireng Salju Bumbu Rujak",
    category: "Snack",
    price: 20000,
    desc: "Cireng kenyal gurih digoreng garing disajikan dengan cocolan sambal rujak pedas manis.",
    image: "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=600&q=80",
    badge: "",
    available: true
  }
];

// BroadcastChannel for instant inter-tab communication (Customer -> Admin)
const channel = typeof BroadcastChannel !== 'undefined' ? new BroadcastChannel('randicafe_sync') : null;

// Storage Keys
const STORAGE_KEYS = {
  MENUS: 'randicafe_menus_v1',
  ORDERS: 'randicafe_orders_v1',
  CART: 'randicafe_cart_v1',
  AUTH: 'randicafe_admin_session_v1',
  CONFIG: 'randicafe_supabase_config_v1'
};

// State Store
const Store = {
  getMenus() {
    const raw = localStorage.getItem(STORAGE_KEYS.MENUS);
    return raw ? JSON.parse(raw) : DEFAULT_MENUS;
  },
  saveMenus(menus) {
    localStorage.setItem(STORAGE_KEYS.MENUS, JSON.stringify(menus));
    if (channel) channel.postMessage({ type: 'MENUS_UPDATED', data: menus });
  },
  getOrders() {
    const raw = localStorage.getItem(STORAGE_KEYS.ORDERS);
    return raw ? JSON.parse(raw) : [];
  },
  saveOrders(orders) {
    localStorage.setItem(STORAGE_KEYS.ORDERS, JSON.stringify(orders));
    if (channel) channel.postMessage({ type: 'ORDERS_UPDATED', data: orders });
  },
  addOrder(order) {
    const orders = this.getOrders();
    orders.unshift(order);
    this.saveOrders(orders);
    this.syncToSupabase(order);
    return order;
  },
  updateOrderStatus(orderId, status) {
    const orders = this.getOrders();
    const target = orders.find(o => o.id === orderId);
    if (target) {
      target.status = status;
      this.saveOrders(orders);
    }
  },
  getCart() {
    const raw = localStorage.getItem(STORAGE_KEYS.CART);
    return raw ? JSON.parse(raw) : [];
  },
  saveCart(cart) {
    localStorage.setItem(STORAGE_KEYS.CART, JSON.stringify(cart));
  },
  clearCart() {
    localStorage.removeItem(STORAGE_KEYS.CART);
  },
  getConfig() {
    const raw = localStorage.getItem(STORAGE_KEYS.CONFIG);
    return raw ? JSON.parse(raw) : { url: '', key: '' };
  },
  saveConfig(cfg) {
    localStorage.setItem(STORAGE_KEYS.CONFIG, JSON.stringify(cfg));
  },
  async syncToSupabase(order) {
    const cfg = this.getConfig();
    if (!cfg.url || !cfg.key) return;
    try {
      const endpoint = `${cfg.url.replace(/\/$/, '')}/rest/v1/pesanan`;
      await fetch(endpoint, {
        method: 'POST',
        headers: {
          'apikey': cfg.key,
          'Authorization': `Bearer ${cfg.key}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=minimal'
        },
        body: JSON.stringify({
          kode_pesanan: order.id,
          nama_pelanggan: order.customerName,
          nomor_meja: parseInt(order.tableNumber) || 0,
          catatan: order.note || '',
          total_harga: order.total,
          status: order.status,
          nama_menu: order.items.map(i => `${i.quantity}x ${i.name}`).join(', '),
          kategori: order.items[0]?.category || 'General',
          jumlah: order.items.reduce((sum, i) => sum + i.quantity, 0),
          harga_satuan: order.items[0]?.price || 0
        })
      });
    } catch (err) {
      console.warn("Supabase background sync notice:", err);
    }
  }
};

// Web Audio API notification chime (no external audio file required)
function playNotificationChime() {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    const ctx = new AudioContext();
    const now = ctx.currentTime;

    const osc1 = ctx.createOscillator();
    const osc2 = ctx.createOscillator();
    const gain = ctx.createGain();

    osc1.type = 'sine';
    osc1.frequency.setValueAtTime(587.33, now); // D5
    osc1.frequency.exponentialRampToValueAtTime(880.00, now + 0.15); // A5

    osc2.type = 'triangle';
    osc2.frequency.setValueAtTime(880.00, now + 0.15);
    osc2.frequency.exponentialRampToValueAtTime(1174.66, now + 0.35); // D6

    gain.gain.setValueAtTime(0.25, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);

    osc1.connect(gain);
    osc2.connect(gain);
    gain.connect(ctx.destination);

    osc1.start(now);
    osc2.start(now + 0.15);
    osc1.stop(now + 0.35);
    osc2.stop(now + 0.6);
  } catch (e) {
    console.log("Audio notice:", e);
  }
}

// Toast helper
function showToast(message, icon = "✓") {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(40px)';
    setTimeout(() => toast.remove(), 300);
  }, 2800);
}

// Price Formatter (IDR)
function formatRupiah(amount) {
  return new Intl.NumberFormat('id-ID', {
    style: 'currency',
    currency: 'IDR',
    maximumFractionDigits: 0
  }).format(amount);
}

// Export global tools
window.RANDICAFE = {
  Store,
  formatRupiah,
  showToast,
  playNotificationChime,
  channel
};
