import React from 'react';
import { motion } from 'framer-motion';

export default function TypingIndicator() {
  return (
    <div className="flex space-x-1 p-2 bg-gray-200 dark:bg-gray-700 rounded-xl w-fit">
      {[0, 1, 2].map((i) => (
        <motion.span
          key={i}
          className="w-2 h-2 bg-gray-500 dark:bg-gray-300 rounded-full"
          animate={{ opacity: [0.3, 1, 0.3], scale: [0.7, 1, 0.7] }}
          transition={{ duration: 1.4, repeat: Infinity, delay: i * 0.2 }}
        />
      ))}
    </div>
  );
}
