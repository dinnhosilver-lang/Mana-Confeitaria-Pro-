import React, { useState } from 'react';
import { Layout, Database, Calculator, Users, CheckCircle, XCircle, Plus, Trash2 } from 'lucide-react';

const App = () => {
  const [activeTab, setActiveTab] = useState('menu');
  const [produtos, setProdutos] = useState([]);
  const [pedidos, setPedidos] = useState([]);
  
  // Estados para formulários
  const [novoProduto, setNovoProduto] = useState({ nome: '', custo: '' });
  const [novoPedido, setNovoPedido] = useState({ cliente: '', telefone: '', produto: '', valor: '', pago: false });

  // Funções de Cadastro
  const adicionarProduto = () => {
    if (novoProduto.nome && novoProduto.custo) {
      setProdutos([...produtos, { ...novoProduto, id: Date.now() }]);
      setNovoProduto({ nome: '', custo: '' });
    }
  };

  const adicionarPedido = () => {
    if (novoPedido.cliente && novoPedido.produto) {
      setPedidos([...pedidos, { ...novoPedido, id: Date.now() }]);
      setNovoPedido({ cliente: '', telefone: '', produto: '', valor: '', pago: false });
    }
  };

  const alternarPagamento = (id) => {
    setPedidos(pedidos.map(p => p.id === id ? { ...p, pago: !p.pago } : p));
  };

  // Renderização das Telas
  return (
    <div className="min-h-screen bg-gray-100 p-4 font-sans">
      <header className="bg-blue-600 text-white p-4 rounded-t-lg shadow-lg">
        <h1 className="text-xl font-bold flex items-center gap-2">
          <Layout size={24} /> Gerenciador de Precificação
        </h1>
      </header>

      {/* Navegação Principal */}
      <nav className="flex bg-white shadow-md mb-6 sticky top-0">
        <button onClick={() => setActiveTab('produtos')} className={`flex-1 p-4 flex flex-col items-center ${activeTab === 'produtos' ? 'border-b-4 border-blue-500 text-blue-500' : 'text-gray-500'}`}>
          <Database size={20} /> <span className="text-xs mt-1">Produtos</span>
        </button>
        <button onClick={() => setActiveTab('precificacao')} className={`flex-1 p-4 flex flex-col items-center ${activeTab === 'precificacao' ? 'border-b-4 border-blue-500 text-blue-500' : 'text-gray-500'}`}>
          <Calculator size={20} /> <span className="text-xs mt-1">Precificar</span>
        </button>
        <button onClick={() => setActiveTab('clientes')} className={`flex-1 p-4 flex flex-col items-center ${activeTab === 'clientes' ? 'border-b-4 border-blue-500 text-blue-500' : 'text-gray-500'}`}>
          <Users size={20} /> <span className="text-xs mt-1">Clientes</span>
        </button>
      </nav>

      <main className="max-w-md mx-auto">
        {/* TELA DE PRODUTOS */}
        {activeTab === 'produtos' && (
          <div className="bg-white p-4 rounded-lg shadow">
            <h2 className="font-bold mb-4">Cadastrar Insumos/Produtos</h2>
            <div className="space-y-3 mb-6">
              <input type="text" placeholder="Nome do item" className="w-full p-2 border rounded" value={novoProduto.nome} onChange={e => setNovoProduto({...novoProduto, nome: e.target.value})} />
              <input type="number" placeholder="Custo (R$)" className="w-full p-2 border rounded" value={novoProduto.custo} onChange={e => setNovoProduto({...novoProduto, custo: e.target.value})} />
              <button onClick={adicionarProduto} className="w-full bg-blue-500 text-white p-2 rounded flex items-center justify-center gap-2">
                <Plus size={18} /> Salvar Produto
              </button>
            </div>
            <ul className="divide-y">
              {produtos.map(p => (
                <li key={p.id} className="py-2 flex justify-between">
                  <span>{p.nome}</span>
                  <span className="font-semibold text-green-600">R$ {parseFloat(p.custo).toFixed(2)}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* TELA DE PRECIFICAÇÃO (SIMPLIFICADA) */}
        {activeTab === 'precificacao' && (
          <div className="bg-white p-4 rounded-lg shadow">
            <h2 className="font-bold mb-4">Cálculo de Venda</h2>
            <p className="text-sm text-gray-500 mb-4 text-justify">Selecione os produtos cadastrados para compor o custo e defina sua margem de lucro.</p>
            {/* Aqui entraria a lógica de seleção de múltiplos produtos do array 'produtos' */}
            <div className="p-4 border-dashed border-2 border-gray-200 rounded text-center text-gray-400">
              Selecione produtos da sua lista para calcular o PV (Preço de Venda).
            </div>
          </div>
        )}

        {/* TELA DE CLIENTES E PEDIDOS */}
        {activeTab === 'clientes' && (
          <div className="space-y-4">
            <div className="bg-white p-4 rounded-lg shadow">
              <h2 className="font-bold mb-4 text-center text-lg">Novo Pedido</h2>
              <div className="grid grid-cols-1 gap-2">
                <input type="text" placeholder="Nome do Cliente" className="p-2 border rounded" value={novoPedido.cliente} onChange={e => setNovoPedido({...novoPedido, cliente: e.target.value})} />
                <input type="text" placeholder="Telefone" className="p-2 border rounded" value={novoPedido.telefone} onChange={e => setNovoPedido({...novoPedido, telefone: e.target.value})} />
                <select className="p-2 border rounded" value={novoPedido.produto} onChange={e => setNovoPedido({...novoPedido, produto: e.target.value})}>
                  <option value="">Selecione o Produto</option>
                  {produtos.map(p => <option key={p.id} value={p.nome}>{p.nome}</option>)}
                </select>
                <input type="number" placeholder="Valor Cobrado (R$)" className="p-2 border rounded" value={novoPedido.valor} onChange={e => setNovoPedido({...novoPedido, valor: e.target.value})} />
                <button onClick={adicionarPedido} className="bg-green-600 text-white p-2 rounded font-bold">Cadastrar Venda</button>
              </div>
            </div>

            <div className="space-y-2">
              {pedidos.map(pedido => (
                <div key={pedido.id} className={`p-4 rounded-lg shadow-md border-l-8 transition-colors ${pedido.pago ? 'bg-green-50 border-green-500' : 'bg-red-50 border-red-500'}`}>
                  <div className="flex justify-between items-start">
                    <div>
                      <p className="font-bold text-lg">{pedido.cliente}</p>
                      <p className="text-sm text-gray-600 italic">{pedido.produto}</p>
                      <p className="text-xs">{pedido.telefone}</p>
                    </div>
                    <div className="text-right">
                      <p className="font-bold text-blue-700">R$ {parseFloat(pedido.valor).toFixed(2)}</p>
                      <button onClick={() => alternarPagamento(pedido.id)} className="mt-2 text-xs flex items-center gap-1 font-medium underline">
                        {pedido.pago ? <><CheckCircle size={14}/> Pago</> : <><XCircle size={14}/> Pendente</>}
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
