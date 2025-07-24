import { useState, useRef, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Send, Loader2 } from 'lucide-react';
import { useTheme } from '../theme';

export default function InputBox({ value, onChange, onSendMessage, isTyping }) {
  const { isDark } = useTheme();
  const textareaRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!value.trim() || isTyping) return;
    onSendMessage(value);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  // Auto-resize textarea
  useEffect(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = `${Math.min(textarea.scrollHeight, 120)}px`;
    }
  }, [value]);

  return (
    <motion.form 
      onSubmit={handleSubmit}
      className={`relative rounded-2xl border transition-all duration-200 ${
        isDark 
          ? 'bg-gray-800 border-gray-700 focus-within:border-blue-500' 
          : 'bg-white border-gray-200 focus-within:border-blue-400'
      } shadow-lg focus-within:shadow-xl`}
      whileFocusWithin={{ scale: 1.02 }}
    >
      <div className="flex items-end p-4 space-x-3">
        <textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={isTyping ? "AI is thinking..." : "Type your message..."}
          disabled={isTyping}
          rows={1}
          className={`flex-1 resize-none border-none outline-none bg-transparent text-sm placeholder-opacity-60 ${
            isDark 
              ? 'text-white placeholder-gray-400' 
              : 'text-gray-900 placeholder-gray-500'
          } disabled:opacity-50`}
          style={{ maxHeight: '120px' }}
        />
        
        <motion.button
          type="submit"
          disabled={!value.trim() || isTyping}
          className={`flex-shrink-0 w-10 h-10 rounded-xl flex items-center justify-center transition-all duration-200 ${
            value.trim() && !isTyping
              ? isDark
                ? 'bg-blue-600 hover:bg-blue-700 text-white shadow-lg hover:shadow-xl'
                : 'bg-blue-500 hover:bg-blue-600 text-white shadow-lg hover:shadow-xl'
              : isDark
                ? 'bg-gray-700 text-gray-500 cursor-not-allowed'
                : 'bg-gray-100 text-gray-400 cursor-not-allowed'
          }`}
          whileHover={value.trim() && !isTyping ? { scale: 1.05 } : {}}
          whileTap={value.trim() && !isTyping ? { scale: 0.95 } : {}}
        >
          {isTyping ? (
            <Loader2 className="w-5 h-5 animate-spin" />
          ) : (
            <Send className="w-5 h-5" />
          )}
        </motion.button>
      </div>
      
      {/* Gradient border effect */}
      <div className={`absolute inset-0 rounded-2xl opacity-0 transition-opacity duration-200 ${
        isDark 
          ? 'bg-gradient-to-r from-blue-500 to-purple-500' 
          : 'bg-gradient-to-r from-blue-400 to-indigo-400'
      } -z-10 blur-sm group-focus-within:opacity-20`} />
    </motion.form>
  );
}
