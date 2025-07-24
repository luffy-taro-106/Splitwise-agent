import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Sun, Moon, Wifi, WifiOff, DollarSign } from 'lucide-react';
import { useTheme } from './theme';
import Chat from './components/Chat';
import InputBox from './components/InputBox';
import QuickActions from './components/QuickActions';

function App() {
  const { theme, toggleTheme } = useTheme();
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    { 
      id: 1, 
      text: "Hi! I'm your Splitwise assistant. How can I help you today?", 
      sender: 'ai',
      timestamp: new Date()
    }
  ]);
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (message) => {
    if (!message.trim()) return;

    const newMessage = { 
      id: Date.now(), 
      text: message, 
      sender: 'user',
      timestamp: new Date()
    };
    setMessages(prev => [...prev, newMessage]);
    setInput('');
    setIsTyping(true);

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });
      const data = await response.json();
      setMessages(prev => [...prev, { 
        id: Date.now() + 1, 
        text: data.response, 
        sender: 'ai',
        timestamp: new Date()
      }]);
      setIsTyping(false);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => [...prev, { 
        id: Date.now() + 1, 
        text: "Sorry, I'm having trouble connecting to the server.", 
        sender: 'ai',
        timestamp: new Date()
      }]);
      setIsTyping(false);
    }
  };

  const handleQuickAction = (action) => {
    const quickMessages = {
      'list-groups': 'Show me all my groups',
      'add-expense': 'I want to add a new expense',
      'recent-expenses': 'Show my recent expenses',
      'balances': 'What are my current balances?'
    };
    
    if (quickMessages[action]) {
      handleSendMessage(quickMessages[action]);
    }
  };

  const isDark = theme === 'dark';

  return (
    <div className={`min-h-screen transition-colors duration-300 ${
      isDark 
        ? 'bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900' 
        : 'bg-gradient-to-br from-blue-50 via-white to-indigo-50'
    }`}>
      {/* Header */}
      <motion.header 
        initial={{ y: -20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        className={`sticky top-0 z-50 backdrop-blur-lg border-b transition-colors duration-300 ${
          isDark 
            ? 'bg-gray-900/80 border-gray-700' 
            : 'bg-white/80 border-gray-200'
        }`}
      >
        <div className="max-w-4xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center">
            <img
              src="/1584483%20(1).png"
              alt="Splitwise logo"
              className="w-8 h-8 mr-3 rounded"/>
            <div>
              <h1 className={`text-xl font-bold ${
                isDark ? 'text-white' : 'text-gray-900'
              }`}>
                Splitwise Assistant
              </h1>
              <p className={`text-sm ${
                isDark ? 'text-gray-400' : 'text-gray-600'
              }`}>
                Manage your expenses with AI
              </p>
            </div>
          </div>
          
          <div className="flex items-center space-x-2">
            <button
              onClick={toggleTheme}
              className={`p-2 rounded-lg transition-colors duration-200 ${
                isDark 
                  ? 'bg-gray-800 hover:bg-gray-700 text-yellow-400' 
                  : 'bg-gray-100 hover:bg-gray-200 text-gray-700'
              }`}
            >
              {isDark ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
            </button>
          </div>
        </div>
      </motion.header>

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-4 py-6 flex flex-col h-[calc(100vh-88px)]">
        {/* Quick Actions */}
        {messages.length === 1 && (
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="mb-6"
          >
            <QuickActions onAction={handleQuickAction} />
          </motion.div>
        )}

        {/* Chat Area */}
        <div className="flex-1 overflow-y-auto mb-4 space-y-4">
          <Chat messages={messages} isTyping={isTyping} />
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.3 }}
        >
          <InputBox 
            value={input}
            onChange={setInput}
            onSendMessage={handleSendMessage}
            isTyping={isTyping}
          />
        </motion.div>
      </div>
    </div>
  );
}

export default App;
